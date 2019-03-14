# def say_hi():
#     print("hi")
#     print("bye")
# say_hi()


# def add_two_number(a, b):
#     print("Tong hai so la:", a+b)
# num1 = int(input("Nhap so thu nhat: "))
# num2 = int(input("Nhap so thu hai: "))
# add_two_number(num1, num2)


# def add_two_number(a,b):
#     return a + b
# num1 = int(input("Nhap so thu nhat: "))
# num2 = int(input("Nhap so thu hai: "))
# num3 = int(input("Nhap so thu ba: "))
# sum_1_2 = add_two_number(num1, num2)
# sum_3 = add_two_number(sum_1_2, num3)
# print("Tong ba so la:", sum_3)


# def abs_of_number(a):
#     if a > 0:
#         return a
#         print("Tri tuyet doi la:", a)
#     else:
#         return -a
#         print("Tri tuyet doi la:", a)
# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)
# print(x)
# print(tong)


# def evaluate (a, b, operator):
#     if operator == "*":
#         return a*b
#     elif operator == "+":
#         return a+b
#     elif operator == "-":
#         return a-b
#     elif operator == "/":
#         return a/b
#     elif operator == "**":
#         return a**b
# print(evaluate (2, 3, "*"))


# t = 0
# n = int(input("Moi nhap so: "))
# for i in range (1, n+1):
#     du = n%i
#     if du == 0:
#         t = t + 1
# if t > 2:
#     print("Day khong phai la so nguyen to.")
# elif n < 2:
#     print("Day khong phai la so nguyen to.")
# else:
#     print("Day la so nguyen to")


def is_prime(n):
    if n < 2:
        return False
    for v in range(2,n):
        if n%v==0:
            return False
    return True
so = int(input("Nhap so can kiem tra: "))

for v in range(2, so+1):
    if is_prime(v):
        print("So nguyen to la:",v)
        
# if is_prime(so):
#     print ("La so nguyen to.")
# else:
#     print("Khong la so nguyen to")







    
    
    


