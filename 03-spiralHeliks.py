import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("gray")
turtle_screen.title("heliks")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle.speed("fastest")

turtle_colors = ["red","blue","pink","orange","black","white","yellow","green"]

for i in range(10):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10*i) #yarıçap bilgisi iister,
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)

turtle.mainloop() #devamlı yapılan işlem oyunun kapanmasını engeller
#turtle.done()
