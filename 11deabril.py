#and, es true si las dos son verdaderas
x= 5
p= x>0
q= x<10
resultado= p and q

print(resultado)

a= True
b= False

print(a and b)
print(a or b)
print(a != b)
print(not a)


edad = 18
tiene_dni = True

if edad >= 18 and tiene_dni:
    print("Puede votar")  
else:
    print("No puede votar")
    


llueve = False
nublado = True
tiempo_al_aire_libre = 30  #minutos

if (llueve or nublado) and tiempo_al_aire_libre > 20:
    print("Llevá paraguas")
else:
    print("No hace falta llevar paraguas")
    


semaforo_parpadeando = True
tiempo_parpadeo = 5  # en segundos
ancho_calle = 10 # en metros
cargando_algo_pesado = False
autos_rapidos = False

if (
    semaforo_parpadeando and
    tiempo_parpadeo <= 5 and
    ancho_calle <= 10 and
    not cargando_algo_pesado and
    not autos_rapidos 
):
    print("Cruzo la calle")
else:
    print("Espero para cruzar")



semaforo_parpadeando = True
tiempo_parpadeo_es_menor_de_5_seg = True  
calle_de_10_metros = True  
sin_carga_pesada = True  
sin_autos_rapidos = True  

if (
    semaforo_parpadeando and
    tiempo_parpadeo_es_menor_de_5_seg and
    calle_de_10_metros and
    sin_carga_pesada and
    sin_autos_rapidos 
):
    print("Cruzo la calle")
else:
    print("Espero para cruzar")


#Forma 2
def puedo_cruzar(semaforo, tiempo, calle, sin_peso, sin_autos):
     if semaforo and tiempo and calle and sin_peso and sin_autos:
           return True
     else:
           return False
if puedo_cruzar(True, True, True, True, True):
     print("Cruzo la calle.")
else:
     print("No cruzo.")


