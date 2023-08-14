# _*_ coding:utf-8 _*_
from flask import Blueprint, send_from_directory

route_static = Blueprint('static', __name__)


@route_static.route('/<path:filename>')
def static(filename):
    print(filename)
    return send_from_directory(app.root_path + '/web/statics/', filename)


from application import app

# 引用路由文件
from web.controllers.index import home

app.register_blueprint(home, url_prefix='/')
