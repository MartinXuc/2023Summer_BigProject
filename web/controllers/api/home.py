import json

from application import app
from flask import jsonify, request, g

from common.libs.Helper import std_resp
from common.libs.UrlManager import UrlManager
from common.models.package.PackageItem import PackageItem
from common.models.package.Package import Package
from common.models.food.food import Food

from web.controllers.api import route_api

# home resource
@route_api.route("/home/resource")
def get_home_res():
    resp = std_resp()
    
    resp['data']['resource'] = app.config['HOME_RES']
    return jsonify(resp)



# home package
@route_api.route("/home/package")
def get_package():
    resp = std_resp()
    package_list = Package.query.filter_by(type=0).all()

    if not package_list:
        resp['code'] = 200
        resp['msg'] = '空'
    
    foodlist = []
    for package in package_list:
        food = Food.query.filter_by(id=package.food_id).first()
        tmp = {
            'id': food.id,
            'name': food.name,
            'imgUrl': UrlManager.build_image_url(food.main_image),
            'price': food.price,
            'discount': package.discount,
            'sale_price': food.price - package.discount
        }
        foodlist.append(tmp)

    resp['msg'] = 'success'
    resp['data'] = foodlist
    return jsonify(resp)
