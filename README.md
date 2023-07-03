# order

## 文件夹/文件

#### common

自定义库

#### web

网站主体, 处理各种请求, 使用common库中提供的功能


###### web/api

提供给前端小程序的接口

web 下的account, finance, food, member, stat, upload, user 为后端管理网站接口


###### web/interceptors

```python-repl
@app.before_request
def before_request():
```

apiautointerceptor.py 验证小程序端是否登录

autointerceptor.py 验证后端是否登录

在请求之前进行用户是否已登录认证, 未登录会重定向至/user/login


###### web/static.py

请求静态资源


###### web/index.py

```python-repl
from flask import g
```

g是全局变量, 可保存用户信息, 每次请求都查询g中信息


#### web/static

静态资源文件, 例如图片等

#### manage.py

Flask的Web开发服务器支持很多启动设置选项，但只能在脚本中作为参数传给app.run()函数。

这种方式很不方便，传递设置选项的理想方式是使用 **命令行参数** 。

实现手段:

```python
from flask_script import Manager
```

导入了一个Manager实例对象, 当调用manager.run()时，就启动了Manager实例接收命令行中的命令。

这些命令需要定义

```python
manager.add_command("hello", Hello()) # 将一个对象设为hello命令, 可在命令行中使用该命令
```

```bash
python manage.py hello
```

#### www.py

mange.py 与 application 构建起网站服务器

www.py 将各种请求与web中的处理函数进行绑定
