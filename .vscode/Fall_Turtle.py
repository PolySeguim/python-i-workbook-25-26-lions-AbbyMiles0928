import turtle

#screen is the object of the Screen class
screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightblue")

#abby is a object of the Turtle class
abby = turtle.Turtle()
abby.shape("turtle")
abby.color("pink")
abby.pensize(2)
abby.speed(100)

def draw_clock():
    for i in range(12):
        abby.penup()
        abby.forward(150)
        abby.pendown()
        abby.stamp()
        abby.penup()
        abby.backward(150)
        abby.right(30)
        abby.forward(150)
        abby.pendown()
        abby.stamp()
        abby.penup()
        abby.backward(150)
#draw_clock()

def draw_clock(t):
    for i in range(12):
        abby.penup()
        abby.forward(150)
        abby.pendown()
        abby.stamp()
        abby.penup()
        abby.backward(150)
        abby.right(30)
        abby.forward(150)
        abby.pendown()
        abby.stamp()
        abby.penup()
        abby.backward(150)

def square_spiral():
    abby.pendown()
    size = 2
    for i in range(1000):
        abby.forward(size)
        abby.right(91)
        size = size + 2
        abby.right(1)
#square_spiral()


def square_spiral2():
    abby.pendown()
    size = 2
    for i in range(1000):
        abby.forward(size)
        abby.right(90)
        size = size + 2
        abby.right(1)  
#square_spiral2()            


def draw_multicolor_square(t,sz):
    """Make Turtle t draw a multi-color square of sz."""
    t.pensize(thickness)
    for i in colors:
        t.color(i)
        t.forward(sz)
        t.left(90)


def getThickness(): 
    thickness = int(input("Enter the thickness of the turtle"))
    return thickness

#TEST SUITE 2
def test2():
    test_turtle = turtle.Turtle()
    test_turtle.shape("turtle")
    test_turtle.color("hotpink")
    color1 = ["red", "blue", "green", "yellow"]
    color2 = ["purple", "orange", "black", "brown"]
    color3 = ["pink", "cyan", "magenta", "lime"]
    thickness = getThickness()
    getThickness()
    draw_multicolor_square(test_turtle, 20,color1)
    draw_multicolor_square(test_turtle, 50,color2)
    draw_multicolor_square(test_turtle, 100,color3)

def draw_square(t, side):
    for i in range(4):
        t.forward(side)
        t.right(90)

def draw_multiple_squares(t, side, num):
    for i in range(num):
        draw_square(t, side)
        t.penup()
        t.forward(side*2)
        t.pendown()

def testy():
    test_turtle = turtle.Turtle()
    test_turtle.shape("turtle")
    test_turtle.color("hotpink")
    test_turtle.pensize(4)
    draw_multiple_squares(test_turtle, 20, 5)
testy()



# TEST SUITE
def test():
    test_turtle = turtle.Turtle()
    test_turtle.shape("turtle")
    test_turtle.color("blue")
    draw_clock(test_turtle)
    draw_clock('t')
    #draw_clock()
    #square_spiral()
    #square_spiral2()


screen.listen()
screen.mainloop()
