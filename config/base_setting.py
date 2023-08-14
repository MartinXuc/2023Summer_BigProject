SERVER_PORT = 80
DEBUG = False
SQLALCHEMY_ECHO = False  # 打印sql语句
AUTH_COOKIE_NAME = 'mooc_food'

# 过滤url
IGNORE_URLS = [
    '^/user/login',
]

# 过滤静态资源
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

# 过滤api
API_IGNORE_URLS = [
    # '^/api'
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    '1': '正常',
    '0': '已删除'
}

# wx小程序配置
MINA_APP = {
    'app_id': 'wxd29bc59e4f792895',
    'app_secret': 'd9e38579606befc209c09d2e52de839f',
    "paykey": "",
    "mch_id": "1443337302",
    "callback_url": "/api/order/callback"
}

# 上传文件配置
UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

APP = {
    # 'domain': 'http://highvorz.website'
    'domain': 'http://192.168.26.11:80'
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "代发货",
    "-6": "待确认",
    "-5": "待评价"
}

