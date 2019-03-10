prices = {
    "banana": 4,
    "apple": 0,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
x = input("Moi nhap ten hang: ")
while x not in prices and stock:
    print("Ban nhap sai roi, moi nhap lai")
    x = input("Moi nhap ten hang: ")
if x in prices and stock:
    print("Price: ", prices[x])
    print("Stock: ", stock[x])
total = 0
for i in prices:
    total = total + (prices[i] * stock[i])

print("So tien kiem duoc la:",total)




    