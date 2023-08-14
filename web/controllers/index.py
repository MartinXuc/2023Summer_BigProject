# -*- coding: utf-8 -*-
import datetime

from flask import Blueprint

from common.libs.Helper import ops_render
from common.models.member.Member import Member
from common.models.pay.PayOrder import PayOrder
from common.models.food.WxShareHistory import WxShareHistory

route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    # 查询今日订单数
    today_pay_orders = PayOrder.query.filter_by(status=1).filter(PayOrder.created_time == datetime.date.today()).all()
    today_pay_orders_nums = len(today_pay_orders)
    # 今日订单金额
    today_pay_orders_money = 0
    for item in today_pay_orders:
        today_pay_orders_money += item.pay_price

    # 查询本月订单数
    month_pay_orders = PayOrder.query.filter_by(status=1).filter(
        PayOrder.created_time >= datetime.date.today().replace(day=1)).all()
    month_pay_orders_nums = len(month_pay_orders)
    # 本月订单金额
    month_pay_orders_money = 0
    for item in month_pay_orders:
        month_pay_orders_money += item.pay_price


    # 查询会员总数
    total_members = Member.query.filter_by(status=1).all()
    total_members_nums = len(total_members)

    # 查询今日新增会员数
    today_members = Member.query.filter_by(status=1).filter(Member.created_time == datetime.date.today()).all()
    today_members_nums = len(today_members)

    # 查询本月新增数
    month_members = Member.query.filter_by(status=1).filter(
        Member.created_time >= datetime.date.today().replace(day=1)).all()
    month_members_nums = len(month_members)

    # 查询今日分享数
    today_share = WxShareHistory.query.filter(WxShareHistory.created_time == datetime.date.today()).all()
    today_share_nums = len(today_share)

    # 查询本月分享数
    month_share = WxShareHistory.query.filter(
        WxShareHistory.created_time >= datetime.date.today().replace(day=1)).all()
    month_share_nums = len(month_share)

    return ops_render("index/index.html",
                      {"total_members_nums": total_members_nums, "today_members_nums": today_members_nums,
                       "month_members_nums": month_members_nums, "today_pay_orders_nums": today_pay_orders_nums,
                       "month_pay_orders_nums": month_pay_orders_nums, "today_pay_orders_money": today_pay_orders_money,
                       "month_pay_orders_money": month_pay_orders_money, "today_share_nums": today_share_nums,
                       "month_share_nums": month_share_nums})
