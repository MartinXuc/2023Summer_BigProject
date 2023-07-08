from application import app
from common.libs.UrlManager import UrlManager


UrlManager.build_res(app.config['HOME_RES'])

# raise ValueError(app.config['HOME_RES'])
