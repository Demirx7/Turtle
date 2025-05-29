import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle pyhton")


t9 = turtle.Turtle()
t9.color("red")


def shrinkingSquare(size):
    for i in range(4):
        t9.forward(size)
        t9.left(90)
        size = size -5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(20)
shrinkingSquare(10)

turtle.done()


