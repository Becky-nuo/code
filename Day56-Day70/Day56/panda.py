import turtle as tt
fn = tt.Turtle()
fn.speed(7)
fn.color("black","black")
fn.pensize(3)

#draw head

fn.circle(100)

#draw right ear

fn.penup()
fn.setx(50)
fn.sety(185)
fn.pendown()
fn.begin_fill()
fn.right(90)
fn.circle(30, -260)
fn.end_fill()

#draw left ear

fn.penup()
fn.setx(-50)
fn.sety(185)
fn.pendown()

fn.left(170)
fn.begin_fill()
fn.right(90)
fn.circle(30, 260)
fn.end_fill()

#draw left eye

fn.penup()
fn.setx(-45)
fn.sety(100)
fn.pendown()
fn.begin_fill()
fn.circle(25)
fn.end_fill()

fn.penup()
fn.setx(-35)
fn.sety(130)
fn.pendown()
fn.color("white")
fn.begin_fill()
fn.circle(7)
fn.end_fill()

#draw right eyezakki.penup()

fn.color("black")
fn.penup()
fn.setx(45)
fn.sety(100)
fn.pendown()
fn.begin_fill()
fn.circle(25)
fn.end_fill()

fn.penup()
fn.setx(35)
fn.sety(130)
fn.pendown()
fn.color("white")
fn.begin_fill()
fn.circle(7)
fn.end_fill()


#draw mouth and nose

fn.color("black")
fn.penup()
fn.setx(0)
fn.sety(80)
fn.pendown()
fn.circle(7)

fn.penup()
fn.setx(0)
fn.setheading(-90)
fn.pendown()
fn.forward(35)

fn.penup()
fn.setx(40)
fn.sety(85)
fn.pendown()
fn.setheading(-270)
fn.circle(40,-180)

tt.done()
