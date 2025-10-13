import turtle

#screen is a complex data type
# meaning that it has attributes and behaviors

# Create a turtle object
# turtle is a complex data type 
My_Turtle = turtle.Turtle()
My_Turtle.color("violet")
My_Turtle.shape("turtle")
# Move the turtle forward by 100 units
def forward100():
    My_Turtle.forward(100)

def right90():
    My_Turtle.right(90)

def left90():
    My_Turtle.left(90)

def backward100():
    My_Turtle.backward(100)


#subjects is a list which is a complex data type
#subjects contains a length of 4
#for loop is for finite loops
#ITERATION - looping through code over and over again

#def subjects = ["math", "science", "health", "economics"]
#for subject in subjects:
    #print("My favorite subject is ", subject)

#counter = 0
#while counter <= (len(subjects)):
    #print("counter: ", counter)
    #increment the counter
    #counter = counter +1

#def rainbow():
    #My_Turtle.forward(-300)
   # My_Turtle.speed(0)
   # colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    #for color in colors:
    #    My_Turtle.color(color)
     #   My_Turtle.pensize(3)
      #  My_Turtle.forward(10)
        #My_Turtle.circle(20)
       # My_Turtle.forward(10)
#rainbow()  

def funActivityWithTurtles():
    size=20 
    #penup and pendown functions
    """
    for i in range(30):
        My_Turtle.penup()
        size = size + 3
        My_Turtle.forward(size)
        My_Turtle.pendown()
        """
    #stamp function
    for i in range(30):
        My_Turtle.penup()        
        My_Turtle.stamp()
        size = size + 3
        My_Turtle.forward(size)
        My_Turtle.right(24)


My_Turtle_2 = turtle.Turtle()
My_Turtle_2.color("pink")
My_Turtle_2.shape("turtle")
My_Turtle_2.speed(3)
My_Turtle_2.pensize(10)

def turtle1000():
    size = 5
    for i in range(1000):
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
        for color in colors: 
            print(color)
            My_Turtle_2.color(color)
            size = size + 1
            My_Turtle_2.forward(size)
            My_Turtle_2.right(50)


# screen is a screen object and it had behaviors
screen = turtle.Screen()
screen.title("Turtle example in python")
#screen.onkey(forward100, "Up")
#screen.onkey(right90, "Right")

screen.listen()
screen.mainloop()

turtle.done()
