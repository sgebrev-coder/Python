price=float(input("Въведете цена на стоката:"))
vat=float(input("Въведете ДДС в проценти:"))
vat_amount=price*vat/100
total_price=price+vat_amount
print(F"Цена на ДДС е: {vat_amount:.2f}")
print(f"Крайна цена с ДДС е: {total_price:.2f}")
