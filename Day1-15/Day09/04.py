
'''
import turtle

t = turtle.Pen()

t.goto(0,0)
t.circle(100)

t.goto(0,-100)
t.circle(200)


t.goto((0,-200)
t.circle(300)
'''



import turtle

t=turtle.Pen()

s=("red","black","yellow","green")

t.width(4)  #画笔的粗细

t.speed(0)  #循环的速度

for i in range(10):  #循环次数
    t.penup()  #抬笔
    t.goto(0,-i*10)
    t.pendown()
    t.color(s[i%len(s)])  #根据不同的数，画笔取不同的颜色
    t.circle(15+i*10) #调整大小
