from application import app
from common.libs.UrlManager import UrlManager


UrlManager.build_res(app.config['HOME_RES'])

swipers = app.config['MENU_SWIPERS']
for i in range(len(swipers)):
    swipers[i] = UrlManager.build_image_url(swipers[i])
    
    