import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("KULAKLIKLIK")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def turtle_rotate_right():
    turtle_instance.setheading(turtle_instance.heading() + 10)

def turtle_rotate_left():
    turtle_instance.setheading(turtle_instance.heading() - 10)


def clear_screen():
    turtle_instance.clear()


def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()




drawing_board.listen()

drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=turtle_rotate_left, key="d")
drawing_board.onkey(fun=turtle_rotate_right, key="a")
drawing_board.onkey(fun=clear_screen, key="s")
drawing_board.onkey(fun=turtle_return_home, key="g")
drawing_board.onkey(fun=turtle_pen_up, key="z")
drawing_board.onkey(fun=turtle_pen_down, key="x")


turtle.mainloop()
