"""dade=20

if idade>=18:
    print("Maior de idade")
else:
    print("Menor de idade")

# The if statement is used to check a condition: if the condition is true, we run a block of code (called the if-block), else we process another block of code (called the else-block). The else clause is optional.

idade=16  

if idade>=18:
    print("Maior de idade")
elif idade>=16: 
    print("Quase maior de idade")
else:
    print("Menor de idade")

contador=10

while contador>0:
    print(contador)
    contador-=1

palavra="python"

for letra in palavra:
    print(letra)

for num in range(1, 10):
    if num == 5:
        break
    if num == 3:
        continue
    print(num)
"""

numero=-0

if numero>0:
    print("positivo")
elif numero<0:  
    print("negativo")
else:
    print("zero")

numeros=[1,2,3,4,5]

for num in numeros:
    if num%2==0:
        print(num, "é par")

contador=1

while contador<10:
    print(contador)
    if contador==5:
        break
    contador+=1
    