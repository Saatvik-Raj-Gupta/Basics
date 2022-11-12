import turtle
from turtle import Screen, Turtle

screen = Screen()
t = Turtle("turtle")
t.speed(-1)


def dragging(x, y):  
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickRight():
    t.clear()


def main(): 
    turtle.listen()

    t.ondrag(dragging)  
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  


main()
