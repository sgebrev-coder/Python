min=float(input("Въведете минути: "))
days=min//(24*60)
hours=min%(24*60)//60
remain_min=min%60
print(f"{min} минути са {days} дни, {hours} часа и {remain_min} минути.")