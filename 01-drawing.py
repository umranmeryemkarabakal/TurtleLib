import turtle

#ekran
drawing_board = turtle.Screen() #turtle ekranı
drawing_board.bgcolor("gray") #ekran bir tanedir,öneden tanımlı renklerdir rgb kodları verilebiliir-hex kodu-
drawing_board.title("Python Turtle")

"""
#turtle
turtle_instance = turtle.Turtle() #kareyi çizen ok,kaplumba
turtle_instance.forward(100) #birden fazla olabilir
turtle_instance2=turtle.Turtle()
turtle_instance2.left(45)#45 derece sola döner
turtle_instance2.forward(100)
#bşladığı noktayı 0,0 alır

#altıgen

turtle_instance = turtle.Turtle()

for i in range(6):
    turtle_instance.forward(150)
    turtle_instance.right(60)
"""

turtle_star = turtle.Turtle()

for i in range(5):
    turtle_star.right(144) #left de denilebilir
    turtle_star.forward(100)

'''
#beşgen
for i in range(5):
    turtle_star.left(72) #right de denilebilir
    turtle_star.forward(100)
'''

#polygon

turtle_instance = turtle.Turtle()
num_sides = 8
angle = 360.0 / num_sides #(yıldız için *5)
side_length = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()#bunu demezsek program kapanır

