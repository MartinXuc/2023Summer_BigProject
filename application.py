import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


# 对Flask类功能的补充
class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(
            import_name,
            template_folder=template_folder,
            root_path=root_path,
            static_folder=None
        )

        # 选择 开发模式配置 or 上线模式配置 
        self.config.from_pyfile('config/base_setting.py')  # 从base_setting.py中加载基础配置
        self.config.from_pyfile('config/resource_setting.py')
        os.environ['ops_config'] = 'local'  # 设置环境变量ops_config为local [local or production]
        if 'ops_config' in os.environ:
            print('config/%s_setting.py' % os.environ['ops_config'])
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])  # 根据环境变量加载对应的配置文件

        # 初始化数据库
        db.init_app(self)  


db = SQLAlchemy()  # 创建SQLAlchemy对象

# __name__ 内置变量
app = Application(__name__, template_folder=os.getcwd() + '/web/templates', root_path=os.getcwd())  # 创建Flask应用程序实例
manager = Manager(app)  # 创建Flask-Script的Manager对象

"""
函数模板
"""
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.build_url, 'build_url')  # 将build_url方法添加为全局模板函数
app.add_template_global(UrlManager.static_url, 'static_url')  # 将static_url方法添加为全局模板函数
app.add_template_global(UrlManager.build_image_url, 'build_image_url')  # 将build_image_url方法添加为全局模板函数
