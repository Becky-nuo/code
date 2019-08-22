


import turtle
import time

turtle.color("purple")  #定义绘制时画笔的颜色

turtle.size(6)  #定义绘制时画笔的线条的宽度
 
turtle.speed(10) #定义绘图的速度

turtle.goto(0,0)  #以0,0为起点进行绘制

 
#绘出正方形的四条边
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

   
#画笔移动到点(-150,-120)时不绘图
turtle.up()
turtle.goto(-150,-120)

turtle.color("red")  #再次定义画笔颜色

 
#在(-150,-120)点上打印"Done"
turtle.write("Done")
time.sleep(3)
