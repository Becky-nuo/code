#找出文本块（收集空行前的所有行并将它们返回）



#文本块生成器

def lines(file):
    for line in file:
        yield line
        yield '\n'
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []




'''
    不需要收集空行，因此不需要返回空文本块（即多个空行）。

    确保文件的最后一行为空行，否则无法确定最后一个文本块到哪里结束。

    生成器lines是个简单的工具，在文件末尾添加一个空行。

    生成器blocks实现了刚才描述的方法。生成文本块时，将其包含的所有行合并，
并将两端多余的空白（如列表项缩进和换行符）删除，得到一个表示文本块的字符串。



'''
