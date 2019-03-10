t=0
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
if x == 4:
    print("Your choice:", x)
    print("Bingo")
    t=t+1
else:
    print("Your choice:", x)
    print(":(")

print("Jack scored these marks in 5 math tests: 49. 81, 72, 66 and 52. What is the mean?")
n = {
    "1.": "About 55",
    "2.": "About 65",
    "3.": "About 75",
    "4.": "About 85"
}
for j in a:
    print(j,n[j])
k = int(input("Nhap cau tra loi cua ban: "))
if k == 2:
    print("Your choice:", k)
    print("Bingo")
    t=t+1
else: 
    print("Your choice:", k)
    print(":(")
if t == 0:
    print("You correctly answer 0 out of 2 questions")
elif t == 1:
    print("You correctly answer 1 out of 2 questions")
else:
    print("You correctly answer 2 out of 2 questions")


