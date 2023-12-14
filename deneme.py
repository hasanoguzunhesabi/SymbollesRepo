from turtle import Turtle
from random import random

t = Turtle()




t.pensize(5)


t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
    t.shape()
    t.towards(4,6)

t.screen.mainloop()

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")