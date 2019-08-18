
#条件循环(重复执行循环体中的语句)

#
import turtle
 
turtle.shape("turtle")
turtle.speed(0)
 
 
def forward(max_distance):
    distance = 0
    step = 1
    while distance < max_distance:
        turtle.forward(step)
        distance += step
 
forward(100)
turtle.exitonclick()



#
import turtle
 
turtle.shape("turtle")
turtle.speed(0)
 
def forward(max_distance, max_radius):
    distance = 0
    step = 1
    while distance < max_distance:
        if turtle.distance(0,0) >= max_radius:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(step)
        distance += step
 
 
forward(550, 100)
turtle.exitonclick()



#
import turtle
import random
 
turtle.shape("turtle")
turtle.speed(0)
 
def forward(max_distance, max_radius):
    distance = 0
    step = 1
    while distance < max_distance:
        if turtle.distance(0,0) >= max_radius:
            angle = turtle.towards(0,0) + random.randint(-45, 45)
            turtle.setheading(angle)
        turtle.forward(step)
        distance += step
 
 
forward(10000, 100)
 
 
turtle.exitonclick()
