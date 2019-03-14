from turtle import *
x=int(input("Nhap x: "))
y=int(input("Nhap y: "))
length=int(input("Nhap chieu dai: "))
def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
mainloop()
draw_star(x,y,length)
