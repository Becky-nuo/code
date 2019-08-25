
import turtle

t=turtle.Turtle()

turtle.setup(300,300,300,100)
t.pensize(2)
t.pencolor('blue')
turtle.tracer(False)
t.penup()
t.begin_poly()   #开始记录多边形的顶点
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_poly()  #获取多边形
shape=t.get_poly()  #注册多边形
turtle.register_shape("shape",shape)
t.pendown()
t.shape('shape')  #绘制这个图形
turtle.tracer(True)
turtle.mainloop()

 
def _destroy(self):
    root = self._root
    if root is _Screen._root:
        Turtle._pen = None
        Turtle._screen = None
        _Screen._root = None
        Screen._canvas = None
    TurtleScreen._RUNNING = False
    root.destroy()

def bye(self):
    """Shut the turtlegraphics window.

    Example (for a TurtleScreen instance named screen):
screen.bye()
        """
    elf._destroy()
turtle.bye()
t.circle(60)
t.pencolor('red')
t.pencolor('#aeffff')
t.pencolor(24,2,255)

def delay(self, delay=None):
    """ Return or set the drawing delay in milliseconds.

    Optional argument:
    delay -- positive integer

    Example (for a TurtleScreen instance named screen):
screen.delay(15)
print(screen.delay())
        """

if delay is None:
    self._delayvalue
    self._delayvalue = int(delay)

   

def _update(self):
        """Perform a Turtle-data update.
        """
screen = self.screen
if screen._tracing == 0:
    return
   
elif screen._tracing == 1:
    self._update_data()
    self._drawturtle()
    screen._update()                  # Turtle
    screen._delay(screen._delayvalue) # Turtle
else:
    self._update_data()
    if screen._updatecounter == 0:
        for t in screen.turtles():
            t._drawturtle()
            screen._update()


def _delay(self, delay):
        """Delay subsequent canvas actions for delay ms."""
self.cv.after(delay)

def _ontimer(self, fun, t):
        """Install a timer, which calls fun after t milliseconds.
        """
if t == 0:
    elf.cv.after_idle(fun)
else:
    self.cv.after(t, fun)
