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


#contraseña con intentos 
contraseña= "milanesa"
entrada= ""
intentos= 0

while entrada != contraseña and intentos < 3:
     entrada = input("Ingrese la contraseña: ")
     if entrada != contraseña:
        print("Contraseña incorrecta")
         intentos +=1
    
print("contraseña correcta")



#adivinar el numero
import random
secreto = random.randint(1, 10)
adivino = False

while not adivino:
    intento = int(input("Adivina el número (entre 1 y 10): "))

    if intento == secreto:
        print("adivinaste")
        adivino = True
    else:
        print("No adivinaste. Intenta de nuevo.")

#adivinar con intentos 
import random
secreto = random.randint(1, 10)
adivino = False
intentos= 0

while not adivino and intentos < 3:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    intentos +=1

    if intento == secreto:
        print("adivinaste")
        adivino = True
    else:
        print("No adivinaste. Intenta de nuevo.")

if not adivino:
    print(f"Se te acabaron los intentos. El número era {secreto}.")
