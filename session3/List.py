ls=[]
n=int(input("Moi ban nhap so phan tu: "))
for i in range(n):
    print("Nhap phan tu thu", i)
    so=int(input(""))
    ls.append(so)
print("Day ban vua nhap la:")
print(ls)
print("Tong day vua nhap:")
print(sum(ls))
print("Phan tu thu 2 trong day:")
print(ls[1])