#创建并填充数据库表(单独编写一个一次性程序)





#将数据导入数据库
import sqlite3

def convert(value):   #函数convert对各行进行分割并对各个字段进行转换
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
        return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''     

        CREATE TABLE food (
        id TEXT PRIMARY KEY,
            desc TEXT,
            water FLOAT,
            kcal FLOAT,
            protein FLOAT,
            fat FLOAT,
            ash FLOAT,
            carbs FLOAT,
            fiber FLOAT,
            sugar FLOAT
            )
            ''')   #将字段中的值插入数据库中

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count = 10

for line in open('文件名.txt'):
    fields = line.split('^')
    vals = [convert(f)for f in fields[:field_count]]
    curs.execute(query, vals)


conn.commit()
conn.close()




'''

    使用curs.executemany，并向它提供一个列表（其中包含从数据文件中提取的所有行）。

    使用网络连接的客户/服务器SQL系统，速度将有极大的提高。

    使用的参数风格为qmark，即使用问号来标记字段。

    如果使用的是较旧的PySQLite版本，可能需要使用字符%来标记字段。



'''
