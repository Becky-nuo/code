#文件



#打开文件(使用函数open，自动导入的模块io中)

f = open('文件名.txt') #文本编辑器创建文件


函数open的参数mode的最常见取值:

        值               描 述
        'r'         读取模式（默认值）
        'w'         写入模式
        'x'         独占写入模式
        'a'         附加模式
        'b'         二进制模式（与其他模式结合使用）
        't'         文本模式（默认值，与其他模式结合使用）
        '+'         读写模式（与其他模式结合使用，表示既可读取也可写入）




'''
    如果文件位于其他地方，可指定完整的路径。

    文件模式调用函数open时，如果只指定文件名，将获得一个可读取的文件对象。
    
    如果要写入文件，必须通过指定模式来显式地指出这一点。
    
    函数open的参数mode的可能取值有多个。

    显式地指定读取模式的效果与根本不指定模式相同。

    在写入模式下打开文件时，既有内容将被删除（ 截断），并从文件开头处开始写入；
如果要在既有文件末尾继续写入，可使用附加模式。

     'r+'和'w+'之间有个重要差别：后者截断文件，而前者不会这样做。

    'rt'，把文件视为经过编码的Unicode文本，自动执行解码和编码，且默认使用UTF-8编码。

    Python使用通用换行模式，换行符（ '\n'、 '\r'和'\r\n'）。


函数open的参数mode的最常见取值:

        值               描 述
        'r'         读取模式（默认值）
        'w'         写入模式
        'x'         独占写入模式
        'a'         附加模式
        'b'         二进制模式（与其他模式结合使用）
        't'         文本模式（默认值，与其他模式结合使用）
        '+'         读写模式（与其他模式结合使用，表示既可读取也可写入）

    

    

'''
