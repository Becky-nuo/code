#繁体字体转换

from zhtools.langconv import *

str1 = "如果你选择和消极、悲观的人在一起，那么他的悲观情绪肯定也会传递给你；但如果你能和快乐的人在一起，那么他的快乐和喜悦势必也会感染到你。"

line = Converter('zh-hant').convert(str1)
print("繁体字-->简体字：\n",line1)  #简体字转繁体字


str2 = "無論你多富有，無論你官多大，角色就是人格。"

line2 = Converter('zh-hant').convert(str2)
print("简体字-->繁体字：\n",line2)  #繁体字转简体字
