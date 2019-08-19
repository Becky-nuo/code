
'''


turtle库基本知识点:

    turtle库是Python标准库之一，是入门级的图形绘制函数库。

    turtle绘图原理：一只海龟在窗体的正中心，在画布上游走，游走的轨迹形成了绘制的图形，海龟是由程序控制的，可以变换颜色、改变宽度等。

    turtle绘图窗体布局：最小单位是像素

    setup():设置窗体大小及位置
    格式：turtle.setup(width,height,startx,starty)。

    4个参数中后两个可选。

    setup函数不是必须使用的，只有需要控制绘图窗体的大小时候才调用。



画笔运动命令:

    turtle.forward(distance) 向当前画笔方向移动distance像素长度

    turtle.backward(distance) 向当前画笔相反方向移动distance像素长度

    turtle.right(degree) 顺时针移动degree°

    turtle.left(degree) 逆时针移动degree°

    turtle.pendown() 移动时绘制图形，缺省时也为绘制

    turtle.goto(x,y) 将画笔移动到坐标为x,y的位置

    turtle.penup() 提起笔移动，不绘制图形，用于另起一个地方绘制

    turtle.circle() 画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆

    setx( ) 将当前x轴移动到指定位置

    sety( ) 将当前y轴移动到指定位置

    setheading(angle) 设置当前朝向为angle角度

    home() 设置当前画笔位置为原点，朝向东。

    dot(r) 绘制一个指定直径和颜色的圆点



画笔控制命令:

    turtle.fillcolor(colorstring) 绘制图形的填充颜色

    turtle.color(color1, color2) 同时设置pencolor=color1, fillcolor=color2

    turtle.filling() 返回当前是否在填充状态

    turtle.begin_fill() 准备开始填充图形

    turtle.end_fill() 填充完成

    turtle.hideturtle() 隐藏画笔的turtle形状

    turtle.showturtle() 显示画笔的turtle形状

    

全局控制命令:

    turtle.clear() 清空turtle窗口，但是turtle的位置和状态不会改变

    turtle.reset() 清空窗口，重置turtle状态为起始状态
    
    turtle.undo() 撤销上一个turtle动作

    turtle.isvisible() 返回当前turtle是否可见

    stamp() 复制当前图形



画布(canvas):

    turtle.screensize(800, 600, "green")

    turtle.screensize() #返回默认大小(400, 300)



画笔控制命令:

    turtle.down() #移动时绘制图形,缺省时也为绘制

    turtle.up() #移动时不绘制图形

    turtle.pensize(width) #绘制图形时的宽度

    turtle.color(colorstring) #绘制图形时的颜色

    turtle.fillcolor(colorstring) #绘制图形的填充颜色

    turtle.fill(Ture)

    turtle.fill(false)



运动命令:

    turtle.forward(degree) #向前移动距离degree代表距离

    turtle.backward(degree) #向后移动距离degree代表距离

    turtle.right(degree) #向右移动多少度

    turtle.left(degree) #向左移动多少度

    turtle.goto(x,y) #将画笔移动到坐标为x,y的位置

    turtle.stamp() #复制当前图形

    turtle.speed(speed) #画笔绘制的速度范围[0,10]整数


    turtle.clear() 清空turtle画的笔迹

    turtle.reset() 清空窗口，重置turtle状态为起始状态

    turtle.undo() (未测试)撤销上一个turtle动作

    turtle.isvisible() (未测试)返回当前turtle是否可见

    turtle.stamp() (未测试)复制当前图形

    turtle.write('vshmily') 写字符串'vshmily'

    turtle.write(s[,font=("font-name",font_size,"font_type")]) (未测试)写文本，s为文本内容，
font是字体的参数，里面分别为字体名称，大小和类型；font为可选项, font的参数也是可选项


    turtle.circle(77) 画一个半径为77的园

    turtle.circle(77, steps=3) 三边形，画一个半径为77的园的内切多边形

    turtle.circle(77, 300) 圆弧为300度



参数:
    radius(半径); 半径为正(负),表示圆心在画笔的左边(右边)画圆
    
    extent(弧度) (optional);
    
    steps (optional) (做半径为radius的圆的内切正多边形,多边形边数为steps)

    radius > 0，逆时针画圆

    radius < 0，顺时针画圆

    extent > 0，取正方向的圆

    extent < 0，取反方向的圆


'''
