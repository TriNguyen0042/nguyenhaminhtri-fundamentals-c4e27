from turtle import *
x=int(input("Nhap x: "))
y=int(input("Nhap y: "))
length=int(input("Nhap chieu dai: "))
def draw_star(x,y,length):
    for i in range(5):
        forward(length)
        right(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()
