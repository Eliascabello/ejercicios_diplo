#explicacion del for
frutas=["manzana","banana","naranja"]

for fruta in frutas:
    print (fruta)
    
for num in range(10):
    print (num)
    
#ejercicio vocales
palabra = "diplomatura"
vocales = "aeiou"
contador= 0
for letra in palabra:
    if letra in vocales:
        contador += 1

print(contador)

#ejercicio par
for numero in range(21):
    if numero % 2 == 0:
        print(numero, end=" ")



