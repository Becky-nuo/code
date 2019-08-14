#添加一些标记(创建简单的标记脚本)


'''

要求:
    `1、设要将第一个文本块放在一级标题标签（ h1）内，而不是段落标签内。
    2、将用星号括起的文本改成突出文本（使用标签em）。''' 



import sys, re
from util import *

print('<html><head><title>...</title><body>')
title = True

for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)#re.sub实现需求的代码较简单
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
        print('</body></html>')



'''

    在Web浏览器中显示这些HTML代码的结果。


基本步骤:

    (1) 打印一些起始标记。
    (2) 对于每个文本块，在段落标签内打印它。
    (3) 打印一些结束标记。
