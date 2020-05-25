count=0
age=20
while count<5:
    count += 1
    guess=int(input("请输入年龄: "))
    if age> guess:
        print( "小了")
    elif age < guess:
        print("大了")
    else:
        print( "对了")
        break