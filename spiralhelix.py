import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("dark blue")
turtle_screen.title("ULAAAN")

turtle_instance = turtle.Turtle()


turtle_colors = ["yellow", "blue", "white", "purple", "orange", "brown"]
turtle.speed(0)
for i in range(17):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.done()