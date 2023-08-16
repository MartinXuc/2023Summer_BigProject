import decimal
import json

from flask import request, g, jsonify

from application import app, db
from common.libs.Helper import std_resp
from common.libs.UrlManager import UrlManager
from common.libs.member.CartService import CartService
from common.libs.pay.PayService import PayService
from common.libs.pay.WeChatService import WeChatService
from common.models.food.food import Food
from common.models.member.OauthMemberBind import OauthMemberBind
from common.models.pay.PayOrder import PayOrder
from web.controllers.api import route_api
from common.libs.pay.PayService import PayService

# 提交订单信息
@route_api.route("/order/info", methods=["POST"])
def order_info():
    '''
        计算订餐的总费用
    '''
    resp = std_resp()
    req = request.values

    if 'goods' not in req:
        resp['code'] = -1
        resp['msg'] = 'empty request'
        return jsonify(resp)
    
    params_goods_list = json.loads(req['Order'])
    
    member_info = g.member_info
    
    food_dic = {item['id']:item['number'] for item in params_goods_list}
    food_list = Food.query.filter(Food.id.in_(food_dic.keys())).all()
    if not food_list:
        resp['code'] = -1
        resp['msg'] = 'error param'
        return jsonify(resp)
     
    data_food_list = []
    yun_price = pay_price = decimal.Decimal(0.00)

    for item in food_list:
        tmp_data = {
            'id': item.id,
            'name': item.name,
            'price': str(item.price),
            'pic_url': UrlManager.build_image_url(item.main_image),
            'number': food_dic[item.id]
        }
        pay_price = pay_price + item.price * int(food_dic[item.id])
        data_food_list.append(tmp_data)

    resp['data']['food_list'] = data_food_list
    resp['data']['pay_price'] = str(pay_price)
    
    resp['data']['total_price'] = str(pay_price + yun_price)
    return jsonify(resp)

# 创建订单
@route_api.route("/order/create", methods=['POST'])
def order_create():
    '''
        创建订单
    '''
    resp = std_resp()
    req = request.values
    
    type = req['type'] if 'type' in req else ''
    note = req['note'] if 'note' in req else ''
    express_address_id = int(req['express_address_id']) if 'express_address_id' in req and req[
        'express_address_id'] else 0
    
    params_goods = req['goods'] if 'goods' in req else None

    if params_goods is None:
        resp['code'] = -1
        resp['msg'] = 'error'
        return jsonify(resp)
    
    items = json.loads(params_goods)
    items = items['order']

    if len(items) < 1:
        resp['code'] = -1
        resp['msg'] = '未选择商品'
        return jsonify(resp)
    member_info = g.member_info
    
    target = PayService()
    params = {
        'note': note,
    }
    resp = target.create_order(member_info.id, items, params)
    
    if resp['code'] == 200 and type == "cart":
        CartService.delete_item(member_info.id, items)
    return jsonify(resp)

# 支付订单
@route_api.route("/order/pay", methods=["POST"])
def orderPay():
    resp = std_resp()
    member_info = g.member_info
    req = request.values
    order_sn = req['order_sn'] if 'order_sn' in req else ''
    pay_order_info = PayOrder.query.filter_by(order_sn=order_sn, member_id=member_info.id).first()
    if not pay_order_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙。请稍后再试"
        return jsonify(resp)
    

    # 设置订单状态为已支付
    pay_order_info.status = 1
    pay_order_info.express_status = 1
    pay_order_info.comment_status = 1
    db.session.add(pay_order_info)
    db.session.commit()

    resp['code'] = 200
    resp['msg'] = 'success'

    # oauth_bind_info = OauthMemberBind.query.filter_by(member_id=member_info.id).first()
    # if not oauth_bind_info:
    #     resp['code'] = -1
    #     resp['msg'] = "系统繁忙。请稍后再试"
    #     return jsonify(resp)

    # config_mina = app.config['MINA_APP']
    # notify_url = app.config['APP']['domain'] + config_mina['callback_url']

    # # 微信支付验证接口
    # # target_wechat = WeChatService(merchant_key=config_mina['paykey'])

    # data = {
    #     'appid': config_mina['appid'],
    #     'mch_id': config_mina['mch_id'],
    #     'nonce_str': target_wechat.get_nonce_str(),
    #     'body': '订餐',  # 商品描述
    #     'out_trade_no': pay_order_info.order_sn,  # 商户订单号
    #     'total_fee': int(pay_order_info.total_price * 100),
    #     'notify_url': notify_url,
    #     'trade_type': "JSAPI",
    #     'openid': oauth_bind_info.openid
    # }

    # pay_info = target_wechat.get_pay_info(pay_data=data)

    # # 保存prepay_id为了后面发模板消息
    # pay_order_info.prepay_id = pay_info['prepay_id']
    # db.session.add(pay_order_info)
    # db.session.commit()

    # resp['data']['pay_info'] = pay_info

    return jsonify(resp)

# 订单结果
@route_api.route("/order/callback", methods=["POST"])
def orderCallback():
    result_data = {
        'return_code': 'SUCCESS',
        'return_msg': 'OK'
    }
    header = {'Content-Type': 'application/xml'}
    config_mina = app.config['MINA_APP']
    target_wechat = WeChatService(merchant_key=config_mina['paykey'])
    callback_data = target_wechat.xml_to_dict(request.data)
    app.logger.info(callback_data)
    sign = callback_data['sign']
    callback_data.pop('sign')
    gene_sign = target_wechat.create_sign(callback_data)
    app.logger.info(gene_sign)
    if sign != gene_sign:
        result_data['return_code'] = result_data['return_msg'] = 'FAIL'
        return target_wechat.dict_to_xml(result_data), header
    if callback_data['result_code'] != 'SUCCESS':
        result_data['return_code'] = result_data['return_msg'] = 'FAIL'
        return target_wechat.dict_to_xml(result_data), header

    order_sn = callback_data['out_trade_no']
    pay_order_info = PayOrder.query.filter_by(order_sn=order_sn).first()
    if not pay_order_info:
        result_data['return_code'] = result_data['return_msg'] = 'FAIL'
        return target_wechat.dict_to_xml(result_data), header

    if int(pay_order_info.total_price * 100) != int(callback_data['total_fee']):
        result_data['return_code'] = result_data['return_msg'] = 'FAIL'
        return target_wechat.dict_to_xml(result_data), header

    if pay_order_info.status == 1:
        return target_wechat.dict_to_xml(result_data), header

    target_pay = PayService()
    target_pay.orderSuccess(pay_order_id=pay_order_info.id, params={"pay_sn": callback_data['transaction_id']})
    # 将微信回调的结果放入记录表
    target_pay.addPayCallbackData(pay_order_id=pay_order_info.id, data=request.data)
    return target_wechat.dict_to_xml(result_data), header
