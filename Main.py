# Case-study #1
# Developers:   Aksenov A. (40%),
#               Soloveychik D. (35%),
#               Labuzov A. (38%)
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
    
    
triangle(297,-150,80,90,'red')
triangle(217,-313,80,270,'yellow')
triangle(278,-258,60,90,'blue')
triangle(326,-318,45,180,'black')
triangle(301,-208,35,45,'pink')
parallelogram(340,-128, 40, 40, 90, 0, 'orange')
parallelogram(299,-91, 40, 40, 60, 0, 'green')

triangle(330,300,70,45,'blue')
triangle(237,340,90,0,'red')
triangle(327,250,90,90,'yellow')
parallelogram(324, 250, 60, 60, 90, 45, 'orange')
parallelogram(214, 294, 50, 50, 60, 0, 'green')
triangle(195,250,40,90,"pink")
triangle(197,210,40,270,"black")

triangle(-50,250,70,270,'yellow')
triangle(-120,320,70,0,'red')
triangle(5,195,55,180,'skyblue')
triangle(-15,194,35,0,'purple')
parallelogram(-50,210,60,40,45,90,'greenyellow')
triangle(-80,179,35,90,'pink')
parallelogram(-22, 350, 40, 40, 90, 45, 'orange')

triangle(-60,-130,50,0,'skyblue')
triangle(-60, -135, 70, 45, 'yellow')
triangle(-10, -285, 70, 225, 'red')
parallelogram(-33, -263, 40, 40, 90, 45, 'orange')
triangle(-90, -265, 40, 45, 'purple')
parallelogram(-8,-290,60,40,45,225,'greenyellow')
triangle(-60,-128,35, 315,'pink')

triangle(-300,-250,70,225,'yellow')
triangle(-297,-150,70,45,'red')
triangle(-400,-150,70,315,'blue')
parallelogram(-300,-150, 40, 70, 120, 180, 'green')
triangle(-383,-225,40,315,'purple')
triangle(-358,-197,40,135,'pink')
parallelogram(-398,-197, 40, 40, 90, 45, 'orange')

triangle(-350,250,70,270,'red')
triangle(-315,280,70,90,'yellow')
triangle(-410,190,30,270,'pink')
triangle(-313,220,50,45,'blue')
triangle(-316,130,30,-135,'purple')
parallelogram(-316, 350, 40, 40, 90, 45, 'orange')
parallelogram(-353, 320, 40, 60, 120, -30, 'green')
