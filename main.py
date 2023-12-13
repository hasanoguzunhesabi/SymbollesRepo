import turtle


drawing_board = turtle.Screen()
drawing_board.bgcolor("#E3773A")
drawing_board.title("Python Turtle")


'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)


turtle_instance.left(90)
turtle_instance.forward(100)

turtle_instance.left(90)
turtle_instance.forward(100)

turtle_instance.left(90)
turtle_instance.forward(100)

turtle.done()
'''

'''
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.left(90)
    turtle_instance.forward(100)
#square
turtle.done()
'''
'''
star_instance = turtle.Turtle()

for star in range(5):
    star_instance.right(144)
    star_instance.forward(200)

turtle.done()
#star
'''
polygon_instance = turtle.Turtle()

num_sides = 9
angle = 360.0 / num_sides * 2
side_length = 100

# 5 is star
for i in range(num_sides):
    polygon_instance.right(angle)
    polygon_instance.forward(side_length)

turtle.done()


