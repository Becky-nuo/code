import random  #导入random，可以产生指定范围内的随机数或字符串；
import string  #导入string，可以打印数字，字符串和特殊字符；
count = 0      #计数器；
while count <3:   #大数据
    car_nums=[]   #存储供用户选择的车牌号
    for i in range(20):  #循环20次车牌号的数字组合
        n1=random.choice(string.ascii_uppercase)  #生成车牌的第一个字母
        n2="".join(random.sample(string.ascii_uppercase+string.digits,5))#车牌的第一个字母和后面的随机5个数字和字母组合的拼接；
        c_num=f"京{n1}-{n2}"   #给c_num赋值;
        car_nums.append(c_num)  #把生成的号码添加到列表里；
        print(i+1,c_num)        #打印车牌号的序列号;
    choice=input("请输入你喜欢的车牌号：").strip() #打印请输入你喜欢的车牌号：并去掉多输入的字符（只会去掉两头的）；
    if choice in car_nums:          #代表合法车牌号；
        print(f"恭喜你选择了新的车牌：{choice}")  #打印你选择的车牌号
        exit("你太幸运了。")          #退出，打印你太幸运了。；
    else:               #否则，(选择不是列表里的车牌号);
        print("不合法的选择" )       #打印不合法;

    count+=1    #循环一次加一(防止死循环);