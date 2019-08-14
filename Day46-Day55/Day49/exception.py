#异常(DB API定义了多种异常)



'''

Python DB API指定的异常（异常层次结构）

            异 常                 超 类                 描 述

            StandardError                           所有异常的超类
            Warning             StandardError       发生非致命问题时引发
            Error               StandardError       所有错误条件的超类
            InterfaceError      Error               与接口（而不是数据库）相关的错误
            DatabaseError       Error               与数据库相关的错误的超类
            DataError           DatabaseError       与数据相关的问题，如值不在合法的范围内
            OperationalError    DatabaseError       数据库操作内部的错误
            IntegrityError      DatabaseError       关系完整性遭到破坏，如键未通过检查
            InternalError       DatabaseError       数据库内部的错误，如游标无效
            ProgrammingError    DatabaseError       用户编程错误，如未找到数据库表
            NotSupportedError   DatabaseError       请求不支持的功能，如回滚

    异常构成了一个层次结构，因此使用一个except块就可捕获多种异常。

    异常应该在整个数据库模块中都可用。


#连接和游标


函数connect的常用参数(字符串)

        参 数 名                描 述             是否可选

        dsn     数据源名称，具体含义随数据库而异    否
        user                用户名                  是
        password            用户密码                是
        host                主机名                  是
        database            数据库名称              是

        

连接对象的方法

            方 法 名                                   描 述
            close()                 关闭连接对象。之后，连接对象及其游标将不可用
            commit()                提交未提交的事务——如果支持的话；否则什么都不做
            rollback()              回滚未提交的事务（可能不可用）
            cursor()                返回连接的游标对象





游标对象的方法:


                名 称                                     描 述
                callproc(name[, params])        使用指定的参数调用指定的数据库过程（可选）
                close()                         关闭游标。关闭后游标不可用
                execute(oper[, params])         执行一个SQL操作——可能指定参数
                executemany(oper, pseq)         执行指定的SQL操作多次，每次都序列中的一组参数
                fetchone()                      以序列的方式取回查询结果中的下一行；如果没有更多的行，就返回None
                fetchmany([size])               取回查询结果中的多行，其中参数size的值默认为arraysize
                fetchall()                      以序列的序列的方式取回余下的所有行
                nextset()                       跳到下一个结果集，这个方法是可选的
                setinputsizes(sizes)            用于为参数预定义内存区域
                setoutputsize(size[, col])      为取回大量数据而设置缓冲区长度



游标对象的属性:

                    名 称                         描 述
                    description         由结果列描述组成的序列（只读）
                    rowcount            结果包含的行数（只读）
                    arraysize           fetchmany返回的行数，默认为1



    要使用底层的数据库系统，必须先连接到它，为此可使用名称贴切的函数connect。

    函数接受多个参数，具体是哪些取决于要使用的数据库。

    函数connect返回一个连接对象，表示当前到数据库的会话。

    方法rollback可能不可用，因为并非所有的数据库都支持事务（ 事务其实就是一系列操作）。

    方法commit总是可用的，但如果数据库不支持事务，这个方法就什么都不做。

    使用游标来执行SQL查询和查看结果，游标支持的方法比连接多，在程序中的地位也可能重要得多。
    



    
'''
