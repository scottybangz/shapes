from turtle import *

print __name__

def draw_triangle(size):
    for i in range(3):
        forward(size)
        left(120)

if __name__ == "__main__":
    draw_triangle(100)

    up()
    forward(200)
    down()

    draw_triangle(100)

    mainloop()
