import turtle

def draw_kite(rosie):
    rosie.right(70)
    rosie.forward(100)
    rosie.right(40)
    rosie.forward(100)
    rosie.right(140)
    rosie.forward(100)
    rosie.right(40)
    rosie.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')
    rosie = turtle.Turtle()
    rosie.shape('turtle')
    rosie.color('blue')
    rosie.speed('normal')
    for i in range(1,37):
        draw_kite(rosie)
        rosie.forward(50)
    window.exitonclick()
draw_art()    
    
      
