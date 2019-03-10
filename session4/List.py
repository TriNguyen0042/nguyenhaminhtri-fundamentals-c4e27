ds=[1,3,7]
for i in range (3):
    for j in range (i+1,3):
        print("i=", i, " j=", j, " cap la:", ds[i],"-",ds[j])
        if (ds[i]+ds[j])%2==0:
                print("cap so can tim la:", ds[i]," ",ds[j])
