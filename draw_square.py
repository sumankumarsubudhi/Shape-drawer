import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('Red')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed('normal')
    for i in range(1,37):
	draw_square(brad)
	brad.right(10)
    # angie = turtle.Turtle()
    # angie.shape('arrow')
    # angie.color('blue')
    # angie.circle(100)

draw_art()
