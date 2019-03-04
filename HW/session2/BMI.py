h = int(input("Chieu cao cua ban?"))
m = int(input("Can nang cua ban?"))
x = h/100
BMI = m/x**2
print (BMI)
if BMI < 16:
    print ("Severely underweight")
elif 18.5 < BMI < 16:
    print ("Underweight")
elif 18.5 < BMI < 25:
    print ("Normal")
elif 25 < BMI <30:
    print ("Overweight")
else:
    print ("Obese")
