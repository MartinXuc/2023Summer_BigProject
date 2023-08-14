from flask import request, jsonify, g
from flask import request, jsonify, g

from application import db
from common.libs.Helper import getCurrentDate, std_resp
from common.libs.member.MemberService import MemberService
from common.models.food.WxShareHistory import WxShareHistory
from common.models.member.Member import Member
from common.models.member.OauthMemberBind import OauthMemberBind
from web.controllers.api import route_api


# 登录即注册
@route_api.route("member/login", methods=['POST'])
def login():
    resp = std_resp()
    req = request.values

    code = req['code'] if req['code'] is not None else None

    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)

    member_id = MemberService.create_new_member(req)
    token = MemberService.get_member_token(member_id)

    resp['data'] = {'token': token}
    return jsonify(resp)


# 验证注册
@route_api.route("/member/check-reg", methods=["GET", "POST"])
def checkReg():
    resp = {'code': 200, 'msg': 'success', 'data': {}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "check-reg"
        return jsonify(resp)

    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)

    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        resp['code'] = -1
        resp['msg'] = "未绑定"
        return jsonify(resp)

    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "未查询到绑定信息"
        return jsonify(resp)
    token = "%s#%s" % (MemberService.gene_auth_code(member_info), member_info.id)
    resp['data'] = {'token': token}
    return jsonify(resp)


@route_api.route("member/check-login")
def check_login():
    resp = std_resp()
    member_info = g.member_info
    if member_info is None:
        resp['msg'] = 'None'
        return jsonify(resp)

    member = {
        'id': member_info.id,
        'name': member_info.name,
    }
    resp['data']['member_info'] = member
    return jsonify(resp)


# 提交分享内容
@route_api.route("/member/share", methods=['POST'])
def memberShare():
    resp = {'code': 200, 'msg': 'success', 'data': {}}
    req = request.values
    url = req['url'] if 'url' in req else ''
    member_info = g.member_info
    model_share = WxShareHistory()
    if member_info:
        model_share.member_id = member_info.id

    model_share.share_url = url
    model_share.created_time = getCurrentDate()
    db.session.add(model_share)
    db.session.commit()
    return jsonify(resp)
