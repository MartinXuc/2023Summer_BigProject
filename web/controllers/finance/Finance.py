# -*- coding: utf-8 -*-
from flask import Blueprint

from common.libs.Helper import ops_render
from common.models.pay.PayOrder import PayOrder
from common.models.pay.PayOrderItem import PayOrderItem
from common.models.food.food import Food
from decimal import Decimal, getcontext
from common.config.base_setting import PAY_STATUS_DISPLAY_MAPPING

route_finance = Blueprint('finance_page', __name__)


@route_finance.route("/index")
def index():
    list = []
    orders = PayOrder.query.all()
    for order in orders:
        order_sn = order.order_sn
        food_id = PayOrderItem.query.filter_by(pay_order_id = order.id).first().food_id
        foodname = Food.query.filter_by(id = food_id).first().name
        price = order.pay_price
        status = order.status
        create_time = order.created_time
        temp = {
            "order_sn": order_sn,
            "foodname": foodname,
            "price": price,
            "status_desc": PAY_STATUS_DISPLAY_MAPPING[str(status)],
            "create_time": create_time
        }
        list.append(temp)
    return ops_render("finance/index.html", {"list": list})


@route_finance.route("/pay-info")
def pay_info():
    return ops_render("finance/pay_info.html")


@route_finance.route("/account")
def account():
    list = []
    orders = PayOrder.query.all()
    # getcontext().prec = 2
    total = Decimal(0)
    for order in orders:
        order_sn = order.order_sn
        food_id = PayOrderItem.query.filter_by(pay_order_id = order.id).first().food_id
        foodname = Food.query.filter_by(id = food_id).first().name
        price = order.pay_price
        status = order.status
        create_time = order.created_time
        temp = {
            "order_sn": order_sn,
            "foodname": foodname,
            "price": price,
            "status_desc": PAY_STATUS_DISPLAY_MAPPING[str(status)],
            "create_time": create_time
        }
        
        list.append(temp)
        # return price
        total = total + Decimal(str(price))
    return ops_render("finance/account.html", {'total': total, 'list': list})
