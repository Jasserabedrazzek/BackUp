import turtle

def draw_heart():
    window = turtle.Screen()
    window.bgcolor("white")

    heart = turtle.Turtle()
    heart.color("red")
    heart.speed(2)
    heart.pensize(2)

    heart.begin_fill()

    # Start drawing the heart
    heart.left(140)
    heart.forward(113)
    for _ in range(200):
        heart.right(1)
        heart.forward(1)
    heart.left(120)
    for _ in range(200):
        heart.right(1)
        heart.forward(1)
    heart.forward(113)

    heart.end_fill()

    heart.hideturtle()
    window.exitonclick()

draw_heart()
