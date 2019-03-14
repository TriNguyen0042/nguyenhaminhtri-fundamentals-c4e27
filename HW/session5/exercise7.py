def remove_dollar_sign(s):
    ns = s.replace("$","")
    return ns
s = input("Nhap ki tu: ")
print(remove_dollar_sign(s))