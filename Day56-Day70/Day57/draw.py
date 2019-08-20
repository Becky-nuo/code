


import turtle

window = turtle.Screen()

bage = turtle.Turtle()

radius = 100
bage.width(3)
bage.color("black", "black")
bage.begin_fill()
bage.circle(radius/2, 180)
bage.circle(radius, 180)
bage.left(180)
bage.circle(-radius/2, 180)
bage.end_fill()

bage.left(90)
bage.up()
bage.forward(radius*0.35)
bage.right(90)
bage.down()
bage.color("white", "white")
bage.begin_fill()
bage.circle(radius*0.15)
bage.end_fill()

bage.left(90)
bage.up()
bage.backward(radius*0.7)
bage.down()
bage.left(90)
bage.color("black", "black")
bage.begin_fill()
bage.circle(radius*0.15)
bage.end_fill()

bage.right(90)
bage.up()
bage.backward(radius*0.65)
bage.right(90)
bage.down()
bage.circle(radius, 180)
bage.ht()
    
window.exitonclick()





