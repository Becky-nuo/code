d = {'1': 'a', '2': 'b', '3': 'c', '4':'d'}

# 使用 for 循环遍历字典
for k in d:
    print("当前的键是 %r, 它的值是：%r" % (k, d.get(k)))


for k, v in d.items():
    print(k, v)
