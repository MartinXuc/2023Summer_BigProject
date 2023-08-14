import time

import qrcode
from flask import jsonify, request, send_from_directory

import barcode
from common.libs.Helper import std_resp
from web.controllers.api import route_api


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
    t = "%04d" % (t % 1000)
    vip_id = "%08d" % (member_info['id'] % 10000000)
    code = vip_id + t

    vip_barcode = barcode.get('ean13', code, writer=barcode.writer.ImageWriter())
    vip_barcode.save('./barcode/' + 'Barcode' + code)

    return send_from_directory('./barcode/', 'Barcode' + code + '.png')


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
    t = "%04d" % (t % 1000)
    vip_id = "%08d" % (member_info['id'] % 10000000)
    code = vip_id + t

    vip_qrcode = qrcode.make()
    with open('./barcode/' + 'QRcode' + code + '.png', 'wb') as f:
        vip_qrcode.save(f)
    return send_from_directory('./barcode/', 'QRcode' + code + '.png')
