import json

from application import app
from flask import jsonify, request, g

from common.models.package.PackageItem import PackageItem
from common.models.package.Package import Package
from common.models.food.food import Food
from common.libs.Helper import std_resp
from common.libs.UrlManager import UrlManager

from web.controllers.api import route_api

# 获取游客优惠券
@route_api.route("/package")
def get_user_package():
    resp = std_resp()
    res = request.values
    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] =  'not logged in'
        return jsonify(resp)
    
    package_list = PackageItem.query.filter_by(member_id = member_info.id).all()

    data = {}
    index = 1
    for item in package_list:
        package = Package.query.filter_by(id = item.package_id).first()
        # raise ValueError(package.id)
        food = Food.query.filter_by(id = package.food_id).first()
        data[index] = {
            'food_id': food.id, 
            'food_name': food.name,
            'imgUrl': food.main_image,
            'price': food.price,
            'discount': package.discount,
            'sale_price': food.price - package.discount,
        }
        index += 1
    resp['data'] = data
    return jsonify(resp)
