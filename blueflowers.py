import turtle
import random

flower = turtle.Turtle()
for n in range(60):
    flower.penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    flower.pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    flower.pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    flower.pensize(random.randint(1, 5))

    for i in range(6):
        flower.circle(circle_size)
        flower.left(60)
