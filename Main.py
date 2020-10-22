import turtle
def triangle(x,y,side,angle,color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(135)
    turtle.forward(side*2**0.5)
    turtle.end_fill()
    turtle.left(225+angle)
    
def parallelogram(x, y, a, b, angle,figang, color):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: length of a longer side
    :param b: length of a shorter side
    :param angle: angle
    :param color: filling color
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pencolor("white")
    turtle.right(angle+figang)
    turtle.forward(a)
    turtle.right(180-angle)
    turtle.forward(b)
    turtle.right(angle)
    turtle.forward(a)
    turtle.right(180-angle)
    turtle.forward(b)
    turtle.left(figang)
    turtle.end_fill()
    
triangle(197+100,-150,80,90,"red")
triangle(197+100-80,-150-163,80,270,"yellow")
triangle(197+100-19,-150-108,60,90,"blue")
triangle(197+100+29,-150-108-60,45,180,"black")
triangle(197+100+4,-150-108+50,35,45,"pink")
parallelogram(194+100+46,-150-108+130, 40, 40, 90, 0, "orange")
parallelogram(194+100+5,-150-108+130+37, 40, 40, 60, 0, "green")

triangle(200+100+30,250+50,70,45,"blue")
triangle(107+100+30,290+50,90,0,"red")
triangle(197+100+30,200+50,90,90,"yellow")
parallelogram(194+100+30, 200+50, 60, 60, 90, 45, "orange")
parallelogram(84+100+30, 244+50, 50, 50, 60, 0, "green")
triangle(65+100+30,200+50,40,90,"pink")
triangle(117+50+30,210,40,270,"black")


