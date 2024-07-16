import random
import sys
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------#
LIMITE_COLA = 100
OCUPADO = 1
LIBRE = 0

if len(sys.argv)!=7 or sys.argv[1]!="-m" or sys.argv[3]!="-s" or sys.argv[5]!="-n":
    print("Uso: python simulacionMM1.py -m <media_intervalo_arrivos> -s <media_tiempo_servicio> -n <numero_atrasos_necesario>")
    sys.exit(1)
media_intarvalo_arrivos = float(sys.argv[2])
media_tiempo_servicio = float(sys.argv[4])
num_atrasos_necesarios = int(sys.argv(6))

tipo_proximo_evento, num_cli_atrasados, num_eventos, num_en_cola, estado_servidor = 0
area_num_en_cola, area_estado_servidor, tiempo_simulacion, tiempo_ultimo_evento, total_retrasos = 0.0
tiempo_proximo_evento = [3]
tiempo_arribo = [LIMITE_COLA + 1]

#-------------------------------------------------------------------------------------------------#
def inicializar():
    tiempo_simulacion = 0.0
    estado_servidor = LIBRE
    num_en_cola = 0
    tiempo_utlimo_evento = 0.0

    num_cli_atrasados = 0
    total_atrasados = 0.0
    area_num_en_cola = 0.0
    area_estado_servidor = 0.0

    tiempo_proximo_evento[1] = tiempo_simulacion + random.expovariate(media_intarvalo_arrivos)
    tiempo_proximo_evento[2] = 1.0e+30

#-------------------------------------------------------------------------------------------------#
def temporizador():
    min_tiempo_proximo_evento = 1.0e+29
    tipo_proximo_evento = 0

    for i in range(1, num_eventos + 1):
        if(tiempo_proximo_evento[i] < min_tiempo_proximo_evento):
            min_tiempo_proximo_evento = tiempo_proximo_evento[i]
            tipo_proximo_evento = i

    if(tipo_proximo_evento == 0):
        print("Pasaron cosas")
        sys.exit(1)
    
    tiempo_simulacion = min_tiempo_proximo_evento

#-------------------------------------------------------------------------------------------------#
def arribo():
    tiempo_proximo_evento[1] = tiempo_simulacion + random.expovariate(media_intarvalo_arrivos)

    if(estado_servidor == OCUPADO):
        num_en_cola = num_en_cola + 1

        if(num_en_cola > LIMITE_COLA):
            print("Pasaron cosas")
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
def reporte():
    print("no hay plata")

#-------------------------------------------------------------------------------------------------#
def actualizacion_tiempo_prom_estadisticas():
    tiempo_desde_ultimo_evento = tiempo_simulacion - tiempo_ultimo_evento
    tiempo_ultimo_evento = tiempo_simulacion
    area_num_en_cola = area_num_en_cola + num_en_cola*tiempo_desde_ultimo_evento
    area_estado_servidor = area_estado_servidor + estado_servidor*tiempo_desde_ultimo_evento

#-------------------------------------------------------------------------------------------------#
#main#
num_eventos = 2
inicializar()
while(num_cli_atrasados < num_atrasos_necesarios):
    temporizador()
    actualizacion_tiempo_prom_estadisticas()
    if(tipo_proximo_evento == 1):
        arribo()
        break
    elif(tipo_proximo_evento == 2):
        salida()
        break
reporte()