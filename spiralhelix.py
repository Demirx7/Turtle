import turtle

board = turtle.Screen()
board.bgcolor("black")
board.title("Pyhton Turtle")

t0 = turtle.Turtle()
t0.color("blue")
turtle.speed(0)

turtle_colors = ["red", "green", "blue","purple","yellow","orange"]


for i in range(6):
    t0.color(turtle_colors[i % 6])
    t0.circle(10 * i)
    t0.circle(-10 * i)
    t0.left(i)

turtle.mainloop()
