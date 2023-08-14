DEBUG = True


HOST_NAME = '127.0.0.1'  # sql host
SQL_PORT = '3306'  # sql port
DB_NAME = 'order'
USERNAME = 'root'
PASSWORD = '123456'

# SQLALCHEMY_ECHO = True  # 打印sql语句
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST_NAME, SQL_PORT, DB_NAME
)


SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ENCODING = "utf-8"
