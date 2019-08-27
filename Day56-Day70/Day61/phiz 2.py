

import turtle
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(200)
 
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(17.5)
turtle.end_fill()
 
turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(17.5)
turtle.end_fill()
 
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-70,steps=3)
 
turtle.penup()
turtle.goto(-100,-70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
turtle.mainloop()#结果如下
