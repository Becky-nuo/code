

import   turtle  as   t 
t.pensize(4)
t.pu()
t.goto(-100,100)
t.setheading(-30)
t.pd()
t.color("black","pink")
t.speed(1)
t.begin_fill()
a=0.4
for  i in   range(120):
    if 0<=i<30  or  60<=i<90:
        t.lt(3)
        a=a+0.08
        t.fd(a)
    else:
        t.lt(3)
        a=a-0.08
        t.fd(a)
t.end_fill()
t.mainloop()
