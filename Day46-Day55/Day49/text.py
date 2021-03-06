#小结

如何创建与关系型数据库交互的Python程序。


概念:

        Python DB API：这个API定义了一个简单的标准化接口，所有数据库包装器模块都必须遵循它，
这让编写使用多个不同数据库的程序更容易。

        连接：连接对象表示到SQL数据库的通信链路，使用方法cursor可从连接获得游标。
你还可使用连接对象来提交或回滚事务。使用完数据库后，就可将连接关闭了。

        游标：游标用于执行查询和查看结果。可逐行取回查询结果，也可一次取回很多（或全部）行。

        类型和特殊值： DB API指定了一组构造函数和特殊值的名称。构造函数用于处理日期和时间对象，
还有二进制数据对象；而特殊值用于表示关系型数据库的类型，如STRING、NUMBER和DATETIME。

        SQLite：这是一个小型的嵌入式SQL数据库，标准Python发行版中包含其Python包装器，
即模块sqlite3。这个数据库速度快、易于使用，且不要求搭建专门的服务器。



函数:


            函 数                     描 述
        connect(...)        连接到数据库并返回一个连接对象
