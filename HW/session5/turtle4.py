from turtle import *
l = input("Do dai canh hinh vuong: ")
c = input("Mau cua vien: ")
def draw_square(l,c):
    color("c")
    begin_fill()
    for i in range(4):
        forward(l)
        left(90)
    end_fill()
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
draw_square(l,c)
