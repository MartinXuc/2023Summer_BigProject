from application import app, manager
from flask_script import Server


import www

# 添加runserver命令到manager
manager.add_command('runserver', Server(
    host='0.0.0.0',
    port=app.config['SERVER_PORT'],
    use_debugger=True
))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()  # 打印错误信息
