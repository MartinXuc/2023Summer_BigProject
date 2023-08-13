
#region debug
DEBUG = True
#endregion

#region database

HOST_NAME = '127.0.0.1'
SQL_PORT = '3306'	
DB_NAME = 'order'
USERNAME = 'root'
PASSWORD = '654321'


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST_NAME, SQL_PORT, DB_NAME
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ENCODING = "utf-8"
#endregion
