while True:
    a = input("Nhap so a: ")
    if a.isdigit():
        a = int(a)
        break
while True:
    b = input("Nhap so b: ")
    if b.isdigit():
        b = int(b)
        break
while True:
    c = input("Nhap so c: ")
    if c.isdigit():
        c = int(c)
        break

D=b**2-4*a*c
if D>0:
    Nghiem1 = (-b+D*0.5)/(2*a)
    Nghiem2 = (-b-D*0.5)/(2*a)
    print ("Nghiem 1 =", Nghiem1)
    print ("Nghiem 2 =", Nghiem2)
elif D<0:
    print("Vo nghiem")
else:
    Nghiem_kep = -b/(2*a)
    print("Nghiem kep =", Nghiem_kep)
