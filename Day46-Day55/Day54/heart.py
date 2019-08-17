

from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')        
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()


#一个正方形+两个半圆

import turtle as t
t.pensize(2)
t.pencolor("red")
t.left(45)
t.fd(200)
t.circle(100, 180)
t.right(90)
t.circle(100, 180)
t.fd(200)
t.done()
