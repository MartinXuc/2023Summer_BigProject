import json

from application import app
from flask import jsonify, request, g

from common.libs.Helper import std_resp
from common.libs.UrlManager import UrlManager

from web.controllers.api import route_api

@route_api.route("/home/resource")
def get_home_res():
    resp = std_resp()
    
    resp['data']['resource'] = app.config['HOME_RES']
    return jsonify(resp)
    

