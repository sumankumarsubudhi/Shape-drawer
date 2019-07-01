import turtle
shape = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    shape.pencolor(colors[x % 6])
    shape.width(x / 100 + 1)
    shape.forward(x)
    shape.left(59)
