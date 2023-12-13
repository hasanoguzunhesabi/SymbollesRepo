import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("DRAWNING")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
def shrinkingSquare(size):
    for kare in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

shrinkingSquare(150)
shrinkingSquare(100)
shrinkingSquare(90)
turtle.done()