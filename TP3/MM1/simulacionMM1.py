import random
import array as arr
import statistics
import math
import sys
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------#
LIMITE_COLA = 100
OCUPADO = 1
LIBRE = 0

if len(sys.argv)!=9 or sys.argv[1]!="-m" or sys.argv[3]!="-s" or sys.argv[5]!="-n" or sys.argv[7]!="-i":
    print("Uso: python simulacionMM1.py -m <media_intervalo_arrivos> -s <media_tiempo_servicio> -n <numero_atrasos_necesario> -i <numero_corridas>")
    sys.exit(1)
media_intarvalo_arrivos = float(sys.argv[2])
media_tiempo_servicio = float(sys.argv[4])
num_atrasos_necesarios = int(sys.argv[6])
nro_corridas = int(sys.argv[8])

tipo_proximo_evento, num_cli_atrasados, num_eventos, num_en_cola, estado_servidor = 0, 0, 0, 0, 0
area_num_en_cola, area_estado_servidor, tiempo_simulacion, total_retrasos = 0.0, 0.0, 0.0, 0.0
tiempo_ultimo_evento = 0.0
tiempo_proximo_evento = [0.0]*3
tiempo_arribo = [0.0]*(LIMITE_COLA + 1)

#-------------------------------------------------------------------------------------------------#
def inicializar():
    global tiempo_simulacion, estado_servidor, num_en_cola, tiempo_ultimo_evento
    global num_cli_atrasados, total_retrasos, area_num_en_cola, area_estado_servidor, tiempo_proximo_evento
    tiempo_simulacion = 0.0
    estado_servidor = LIBRE
    num_en_cola = 0
    tiempo_ultimo_evento = 0.0

    num_cli_atrasados = 0
    total_retrasos = 0.0
    area_num_en_cola = 0.0
    area_estado_servidor = 0.0

    tiempo_proximo_evento[1] = tiempo_simulacion + random.expovariate(media_intarvalo_arrivos)
    tiempo_proximo_evento[2] = 1.0e+30


#-------------------------------------------------------------------------------------------------#
def temporizador():
    
    global tiempo_simulacion, tipo_proximo_evento
    min_tiempo_proximo_evento = 1.0e+29
    tipo_proximo_evento = 0

    for i in range(1, num_eventos + 1):
        if(tiempo_proximo_evento[i] < min_tiempo_proximo_evento):
            min_tiempo_proximo_evento = tiempo_proximo_evento[i]
            tipo_proximo_evento = i

    if(tipo_proximo_evento == 0):
        f.write("\nLista de Eventos vacia en tiempo"+str(tiempo_simulacion))
        sys.exit(1)
    
    tiempo_simulacion = min_tiempo_proximo_evento

#-------------------------------------------------------------------------------------------------#
def arribo():
    global tiempo_simulacion, num_en_cola, estado_servidor, total_retrasos, num_cli_atrasados, tiempo_proximo_evento
    tiempo_proximo_evento[1] = tiempo_simulacion + random.expovariate(media_intarvalo_arrivos)

    if(estado_servidor == OCUPADO):
        num_en_cola = num_en_cola + 1

        if(num_en_cola > LIMITE_COLA):
            f.write("\nOverflow del array tiempo_arribo en tiempo"+str(tiempo_simulacion))
            sys.exit(1)
        
        tiempo_arribo[num_en_cola] = tiempo_simulacion
    
    else:
        demora = 0.0
        total_retrasos = total_retrasos + demora
        num_cli_atrasados = num_cli_atrasados + 1
        estado_servidor = OCUPADO
        tiempo_proximo_evento[2] = tiempo_simulacion + random.expovariate(media_tiempo_servicio)

#-------------------------------------------------------------------------------------------------#
def salida():
    global num_en_cola, estado_servidor, tiempo_proximo_evento, tiempo_arribo, total_retrasos, num_cli_atrasados
    if(num_en_cola == 0):
        estado_servidor = LIBRE
        tiempo_proximo_evento[2] = 1.0e+30
    else:
        num_en_cola = num_en_cola - 1
        atraso = tiempo_simulacion - tiempo_arribo[1]
        total_retrasos = total_retrasos + atraso
        num_cli_atrasados = num_cli_atrasados + 1
        tiempo_proximo_evento[2] = tiempo_simulacion + random.expovariate(media_tiempo_servicio)
        
        for i in range(1,num_en_cola + 1):
            tiempo_arribo[i] = tiempo_arribo[i + 1]

#-------------------------------------------------------------------------------------------------#
def reporte(x):
    f.write("\nResultados para corrida numero: "+str(x+1)+" --------------------------------------------------\n")
    f.write("\nTiempo promedio de demora en cola "+str(total_retrasos/num_cli_atrasados)+" minutos\n")
    f.write("\nNumero promedio en cola "+str(area_num_en_cola/tiempo_simulacion)+"\n")
    f.write("\nUtilizacion del servidor "+str(area_estado_servidor/tiempo_simulacion)+"\n")
    f.write("\nTiempo de simulacion finalizada "+str(tiempo_simulacion)+" minutos\n")

#-------------------------------------------------------------------------------------------------#
def actualizacion_tiempo_prom_estadisticas():
    global tiempo_ultimo_evento, area_num_en_cola, area_estado_servidor, tiempo_simulacion
    tiempo_desde_ultimo_evento = tiempo_simulacion - tiempo_ultimo_evento
    tiempo_ultimo_evento = tiempo_simulacion
    area_num_en_cola = area_num_en_cola + num_en_cola*tiempo_desde_ultimo_evento
    area_estado_servidor = area_estado_servidor + estado_servidor*tiempo_desde_ultimo_evento

#-------------------------------------------------------------------------------------------------#
#main#
f = open("reporte.txt", "w")
i=0
eje_x = []
eje_y = []
eje_y_serv = []
num_eventos = 2
f.write("Sistema de colas con unico servidor\n\n")
f.write("Media de tiempo entre entre arribos " + str(media_intarvalo_arrivos) + " minutos\n")
f.write("Media de tiempo de servicio " + str(media_tiempo_servicio) + " minutos\n")
f.write("Numero de clientes " + str(num_atrasos_necesarios) + "\n")
t = plt.figure(1)
t2 = plt.figure(2)
for x in range(nro_corridas):
    eje_x = []  
    eje_y = []
    eje_y_serv = []
    inicializar()
    while(num_cli_atrasados < num_atrasos_necesarios):
        eje_x.append(tiempo_simulacion)
        eje_y.append(num_en_cola)
        eje_y_serv.append(estado_servidor)
        temporizador()
        actualizacion_tiempo_prom_estadisticas()
        if(tipo_proximo_evento == 1):
            arribo()
            
        elif(tipo_proximo_evento == 2):
            salida()
        i = i + 1   
    reporte(x)
    plt.figure(1)
    plt.step(eje_x,eje_y, color = "C" + str(x % 10), label = "corrida nro"+str(x))
    plt.figure(2)
    plt.step(eje_x,eje_y_serv, color = "C" + str(x % 10), label = "corrida nro"+str(x))
plt.figure(1)
plt.legend()
t.savefig("grafica_numero_clientes_en_cola.jpg")
plt.figure(2)
plt.legend()
t2.savefig("grafica_ocupacion_servidor.jpg")
f.close()
