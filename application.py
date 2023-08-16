import os

from flask import Flask
from flask_script import Manager

from common.models.db import db
from common.config.base_setting import APP


# app 对象
# Flask的功能个性化
class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(
            import_name,
            template_folder=template_folder,
            root_path=root_path,
            static_folder=None
        )

        # app.config 初始化
        self.config.from_pyfile('common/config/base_setting.py')  # 从base_setting.py中加载基础配置
        self.config.from_pyfile('common/config/resource_setting.py')

        os.environ['ops_config'] = 'local'  # 设置环境变量ops_config为local [local or production]

        # os.environ: 环境变量
        if 'ops_config' in os.environ:
            print('common/config/%s_setting.py' % os.environ['ops_config'])
            self.config.from_pyfile('common/config/%s_setting.py' % os.environ['ops_config'])  # 根据环境变量加载对应的配置文件

        # 配置
        APP['root_path'] = self.root_path
        
        # 初始化数据库
        # 相当于 db = SQLALchemy(app)
        
        db.init_app(self)  



# 创建app对象
app = Application(__name__, template_folder=os.getcwd() + '/web/templates', root_path=os.getcwd())  # 创建Flask应用程序实例
manager = Manager(app)  # 创建Flask-Script的Manager对象


from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.build_url, 'build_url')  # 将build_url方法添加为全局模板函数
app.add_template_global(UrlManager.static_url, 'static_url')  # 将static_url方法添加为全局模板函数
app.add_template_global(UrlManager.build_image_url, 'build_image_url')  # 将build_image_url方法添加为全局模板函数
