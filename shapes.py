from turtle import *

fillLine = "white"

def triangleFill(size, fillLine):
    color(fillLine)
    begin_fill()
    setheading()
    forward(size)
    setheading(120)
    forward(size)
    setheading(240)
    forward(size)
    end_fill()

if __name__ == "__main__":

    mainloop()
