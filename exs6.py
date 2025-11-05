value1=(input("Въведете първата валута:"))
value2=(input("Въведете втората валута:"))
conversion_rate=float(input("Въведете курс на конверсия:"))
sum=float(input(f"Въведете сума за конверсия:", {value1}))
converted_amount=sum*conversion_rate
print(f"{value1} към {value2} е: {converted_amount:.2f}")