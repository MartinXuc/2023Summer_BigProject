import os
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',  # 主机名
    port=3306,         # 端口号，MySQL默认为3306
    user='root',       # 用户名
    password='654321', # 密码
)
current_dir = os.path.dirname(__file__)
cursor = conn.cursor()

# execute sql
def do_sql(file):
    file = current_dir + file
    with open(file, 'r') as f:
            sql_list = f.read().split(';')
            sql_list = [x.strip() for x in sql_list if x.strip()]
            for sql in sql_list:
                cursor.execute(sql)


# 执行目录下sql语句
def do_dir_sql(relative_path):
    absolute_path = current_dir + relative_path
    print(absolute_path)
    sql_files = os.listdir(absolute_path)
    
    for item in sql_files: 
        file = relative_path + '/' + item
        do_sql(file)

# 删除数据库
def clear_all():
    do_sql('/clear.sql')
    conn.commit()

# 创建数据库以及插入数据
def initial():
    do_sql('/create_database.sql')
    cursor.execute("use `order`;")
    do_dir_sql('/create')
    do_dir_sql('/insert')
    do_sql('/after_create.sql')
    conn.commit()



# command
cursor.execute("use `order`;")
do_dir_sql('/create')
do_dir_sql('/insert')
conn.commit()

cursor.close()
conn.close()
