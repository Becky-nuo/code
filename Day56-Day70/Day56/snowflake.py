

import turtle as t
def koch(size,n):
	if n==0:
		t.fd(size)
	else:
		for angle in [0,60,-120,60]:
			t.left(angle)
			koch(size/3,n-1)

			
t.setup(800,400)
t.penup()
t.goto(-500,150)
t.pd()
t.pensize(2)
koch(400,3)
t.right(120)
koch(400,3)
t.right(120)
koch(400,3)
t.right(120)
t.hideturtle()
t.done()
 
