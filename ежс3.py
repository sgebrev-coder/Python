km=float(input("Въведете изминати километри:"))
fuel=float(input("Въведете изразходвано гориво в литри:"))
consumption=(fuel/km)*100
print(f"Среден разход на гориво: {consumption:.2f} ")
km1=float(input("Въведете километри:"))
fuel_need=(consumption/100)*km1
print(f"Необходими литри гориво: {fuel_need:.2f} ") 
fuel_type=input("Въведете вид гориво (бензин/дизел):")
if fuel_type=="бензин":
    price_per_liter=2.20
elif fuel_type=="дизел":
    price_per_liter=2.50
total_cost=fuel_need*price_per_liter
print(f"Обща стойност на горивото: {total_cost:.2f} лева")
