#finally子句(用于在发生异常时执行清理工作,与try子句配套的)



x = None
try:
    x = 1 / 0
finally:
    print('Cleaning up ...')
    del x
'''不管try子句中发生什么异常，都将执行finally子句'''



try:
    1 / 0
except NameError:
    print("Unknown variable")
else:
    pint("That went well!")
finally:
    print("Cleaning up.")


'''
    虽然使用del来删除变量是相当愚蠢的清理措施，
但finally子句非常适合用于确保文件或网络套接字等得以关闭。


    可在一条语句中同时包含try、 except、 finally和else（或其中的3个）。
'''
