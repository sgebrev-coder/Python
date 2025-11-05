n=int(input("Въведете брой елементи в списъка: "))
a=[]
for i in range(n):
    element=int(input(f"Въведете елемент {i}: "))
    a.append(element)
print(f"Списъкът е: {a}")

d=0
for x in a:
  if x % 3==0:
    d+=1
    
print(" Брой лементи ", d)
  
