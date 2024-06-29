import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("orange")
turtle_screen.title("shrinking square")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")

def shrinkSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.right(90)
        size = size - 5

x = 200
for i in range(20):
    shrinkSquare(x)
    x = x - 20

turtle.done()