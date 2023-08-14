from flask import jsonify, request, g

from common.libs.Helper import std_resp
from web.controllers.api import route_api

from common.libs.chat.chat import *


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
