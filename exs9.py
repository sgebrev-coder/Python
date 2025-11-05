a=float(input("Въведете число а:"))
b=float(input("Въведете число b:"))
if b==0:
    print("Грешка: Не може да се дели на нула.")
else:
    quatient=a//b
    remainder=a%b
    print(f"{a}/{b}={quatient} с остатък {remainder}")