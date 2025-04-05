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

#while condicion
contador=0

while contador < 5:
    print(contador)
    contador +=1
    
#while True:
    print(contador)
    contador+=1
    if contador==5:
        break# 

contador = 1

while contador <= 10:
    print(contador)
    contador += 1
    
contador = 1

#break para que corte
while True:
    print(contador)
    contador += 1
    if contador > 10:
        break

#ejercicio de contraseña con while 
contraseña= "milanesa"

entrada= ""

while entrada != contraseña:
     entrada = input("Ingrese la contraseña: ")
     if entrada != contraseña:
        print("Contraseña incorrecta")
    
print("contraseña correcta")


