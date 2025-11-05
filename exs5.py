num=[]
for i in range(3):
 n=float(input(f"Въведете число: {i+1}"))
 num.append(n)

avarage=sum(num)/3
print(f"Средно статистическото е: {avarage:.2f}")
