#类型

'''

DB API构造函数和特殊值


                名 称                                 描 述
            Date(year, month, day)              创建包含日期值的对象

            Time(hour, minute, second)          创建包含时间值的对象
            
            Timestamp(y, mon, d, h, min, s)     创建包含时间戳的对象
            
            DateFromTicks(ticks)                根据从新纪元开始过去的秒数创建包含日期值的对象
            
            TimeFromTicks(ticks)                根据从新纪元开始过去的秒数创建包含时间值的对象
            
            imestampFromTicks(ticks)            根据从新纪元开始过去的秒数创建包含时间戳的对象
            
            Binary(string)                      创建包含二进制字符串值的对象
            
            STRING                              描述基于字符串的列（如CHAR）
            
            BINARY                              描述二进制列（如LONG或RAW）
            
            NUMBER                              描述数字列
            
            DATETIME                            描述日期/时间列
            
            ROWID                               描述行ID列



    插入到某些类型的列中的值，底层SQL数据库可能要求它们满足一定的条件。

    与底层SQL数据库正确地互操作， DB API定义了一些构造函数和常量（单例），用于提供特殊的类型和值。

    在数据库中添加日期，应使用相应数据库连接模块中的构造函数Date来创建它，这让连接模块能够在幕后执行必要的转换。

    每个模块都必须实现构造函数和特殊值。


'''




