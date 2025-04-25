import csv 
archivo_csv= open ("C:/Users/Eliasbc/Desktop/archivos/dns.csv")
archivo= csv.reader(archivo_csv, delimiter=";")

for f in archivo: 
    IP1=f[0]
    oficina=f[1]
    trafico=0
    archivo_csv2= open ("C:/Users/Eliasbc/Desktop/archivos/trafico.csv")
    archivo2= csv.reader(archivo_csv2, delimiter=";")
    for f2 in archivo2:
        IP2= f2 [0]
        consumo=int(f2[1])
        if IP1==IP2:
            trafico+=consumo
    archivo_log = f"la IP {IP1} consumio {trafico}\n"
    print(archivo_log)
archivo_csv.close()
archivo_csv2.close()