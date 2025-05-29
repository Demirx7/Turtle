import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green2")
drawing_board.title("Square")
t1 = turtle.Turtle()
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.left(90)
t1.forward(100)

turtle.done()


for i in range(4):
    t1.forward(100)
    t1.left(90)

board = turtle.Screen()
board.bgcolor("green2")
board.title("Star")

t5 = turtle.Turtle()
for i in range(5):

    t5.forward(300)
    t5.right(144)


turtle.done()


