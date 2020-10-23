import turtle
def triangle(x,y,side,angle,color):
    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side: length of a side
    :param angle: angle
    :param color: filling color
    :return: None
    '''
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
    :param angle: angle inside figure
    :param figang: angle of a figure
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

triangle(100 - 150,100 + 150,70,270,'yellow')
triangle(30 - 150,170 + 150,70,0,'red')
triangle(155 - 150,45 + 150,55,180,'skyblue')
triangle(135 - 150,44 + 150,35,0,'purple')
parallelogram(100 - 150,60 + 150,60,40,45,90,'greenyellow')
triangle(70 - 150,29 + 150,35,90,'pink')
parallelogram(128 - 150, 200 + 150, 40, 40, 90, 45, 'orange')

triangle(-60,-130,50,0,'skyblue')
triangle(-60, -135, 70, 45, 'yellow')
triangle(-10, -285, 70, 225, 'red')
parallelogram(-33, -263, 40, 40, 90, 45, 'orange')
triangle(-90, -265, 40, 45, 'purple')
parallelogram(-8,-290,60,40,45,225,'greenyellow')
triangle(-60,-128,35, 315,'pink')

triangle(-300,-250,70,225,'yellow')
triangle(-300+3,-250+100,70,45,'red')
triangle(-300-100,-250+100,70,315,'blue')
parallelogram(-300,-250+100, 40, 70, 120, 180, "green")
triangle(-300-50-33,-250+45-20,40,315,'purple')
triangle(-300-50-33+25,-250+45-20+28,40,315-180,'pink')
parallelogram(-300-50-33+25-40,-250+45-20+28, 40, 40, 90, 45, "orange")

triangle(-200 - 150,100 + 150,70,270,'red')
triangle(-200-150+35,100+150+30,70,90,"yellow")
triangle(-200-150+30-90,100+150-60,30,270,"pink")
triangle(-200-150+30-80+87,100+150-50+20,50,45,"blue")
triangle(-200-150+30-80+84,100+150-50+20-90,30,-135,"purple")
parallelogram(-200-150+30-80+84, 100+150-50+20-70+200, 40, 40, 90, 45, "orange")
parallelogram(-200-150+30-80+84-37, 100+150-50+20-70+200-30, 40, 60, 120, -30, "green")
