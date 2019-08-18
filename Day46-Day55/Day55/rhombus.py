

import turtle


t = turtle.Pen()
colors=['red','green','blue']
for x in range(360):
    t.pencolor(colors[x%3])
    t.forward(x)
    t.left(121)
input('press any key')
 
