from flask import Blueprint, send_from_directory
from application import app

route_static = Blueprint('static', __name__)


# 请求静态资源
@route_static.route('/<path:filename>')
def index(filename):
    app.logger.info(filename)
    return send_from_directory(app.root_path + '/web/static', filename)
