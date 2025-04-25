'''archivo=open ('lenguajes.txt','r')
lineas = archivo. readlines()
print(lineas)
archivo.close()

with open('lenguajes.txt','r') as archivo:
    lineas=archivo.readlines()

for 1 in lineas:
    print (1)
'''
with open('lenguajes.txt','r') as archivo:
    print(type(archivo.read()))

with open('mis_datos','w') as archivo:
    archivo.write("Elias\nCabello")