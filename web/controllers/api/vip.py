from flask import g, jsonify, request, send_from_directory, Response

from application import app
from common.libs.Helper import select_filter_obj, get_dict_filter_field, std_resp
from common.libs.UrlManager import UrlManager
from common.models.food.food import Food
from common.models.pay.PayOrder import PayOrder
from common.models.pay.PayOrderItem import PayOrderItem
from web.controllers.api import route_api

import time
import barcode
import qrcode

# barcode
@route_api.route("/vip/barcode")
def getBarcode():
    resp = std_resp()
    member_info = {
        'id': 1
    }
    member_info['id'] = 1
    req = request.values

    
    if not member_info:
        resp['msg'] = '未登录'
        return jsonify(resp)
    
    
    t = time.time()
    t = "%04d" % (t%1000)
    vip_id = "%08d" % (member_info['id'] % 10000000)
    code = vip_id + t
    
    vip_barcode = barcode.get('ean13', code, writer=barcode.writer.ImageWriter())
    vip_barcode.save('./output/barcode/' + 'Barcode' + code)
    
    return send_from_directory('./output/barcode/', 'Barcode' + code + '.png')


# QRcode
@route_api.route("/vip/qrcode")
def getQRcode():
    resp = std_resp()
    member_info = {
        'id': 1
    }
    member_info['id'] = 1
    req = request.values

    if not member_info:
        resp['msg'] = '未登录'
        return jsonify(resp)
    
    t = time.time()
    t = "%04d" % (t%1000)
    vip_id = "%08d" % (member_info['id'] % 10000000)
    code = vip_id + t

    vip_qrcode = qrcode.make()
    with open('./output/barcode/' + 'QRcode' + code + '.png', 'wb') as f:
        vip_qrcode.save(f)
    return send_from_directory('./output/barcode/', 'QRcode' + code + '.png')
