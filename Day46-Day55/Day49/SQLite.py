#13.2 SQLite 和 PySQLite


'''
    数据库引擎大都作为服务器程序运行，连安装都需要有管理员权限。

    为降低Python DB API的使用门槛，选择SQLite的小型数据库引擎。

    SQLite，不需要作为独立的服务器运行，且可直接使用本地文件，而不需要集中式数据库存储机制。

'''


#起步

 
import sqlite3   #模块sqlite3
conn = sqlite3.connect('somedatabase.db')

#游标
curs = conn.cursor()        #这个游标可用来执行SQL查询。


conn.commit()  #提交


conn.close()  #关闭连接


'''
    使用Python标准库中的SQLite，可通过导入模块sqlite3来导入它，就可创建直接到数据库文件的连接。

    需提供一个文件名（可以是文件的相对路径或绝对路径）；如果指定的文件不存在，将自动创建它。




'''
