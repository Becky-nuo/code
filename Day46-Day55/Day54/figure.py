
#简单图形
import turtle
def drawSquare(sides,length):
  angle = 360/sides
  for again in range(sides):      
      turtle.forward(length)
      turtle.right(angle)
def moveTurtle(x,y):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
drawSquare(4,40)
moveTurtle(100,100)
drawSquare(4,40)
moveTurtle(-100,100)
drawSquare(4,40)
turtle.done()
