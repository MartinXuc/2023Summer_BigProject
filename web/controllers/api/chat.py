import json

from application import app
from flask import jsonify, request, g

from common.models.package.PackageItem import PackageItem
from common.models.package.Package import Package
from common.models.food.food import Food
from common.libs.Helper import std_resp
from common.libs.UrlManager import UrlManager

from common.libs.chat.chat import *

from web.controllers.api import route_api


@route_api.route("/guide", methods=['POST'])
def chat():
    resp = std_resp()
    res = request.values
    member_info = g.member_info
    
    question = res['msg']
    # answer = Chat.answer(question)
    answer = '抱歉, 我不明白.'
    resp['question'] = question
    resp['answer'] = answer
    return jsonify(resp)
