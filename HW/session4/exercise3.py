print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x + 3) ?")
a = {
    "1.":"35",
    "2.":"36",
    "3.":"40",
    "4.":"44"
}
for i in a:
    print(i,a[i])
x = int(input("Nhap cau tra loi cua ban: "))
if x==4:
    print("Your choice:", x)
    print("Bingo")
else:
    print("Your choice:",x)
    print(":(")