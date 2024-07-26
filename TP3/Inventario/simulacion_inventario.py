import random
import array as arr
import statistics
import math
import sys
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------#
if len(sys.argv)!=25 or sys.argv[1]!="-a" or sys.argv[3]!="-b" or sys.argv[5]!="-c" or sys.argv[7]!="-d" or sys.argv[9]!="-e" or sys.argv[11]!="-f" or sys.argv[13]!="-g" or sys.argv[15]!="-h" or sys.argv[17]!="-i" or sys.argv[19]!="-j" or sys.argv[21]!="-k" or sys.argv[23]!="-l":
    print("Uso: python simulacion_inventario.py -a <nivel inicial de inventario> -b <meses por pedido> -c <num_policies> -d <valores de demanda> -e <media intervalo demanda> -f <costo de setup> -g <costo incremental> -h <costo de mantenimiento> -i <costo por faltante> -j <minlag> -k <maxlag> -l <numero de corridas>")
    sys.exit(1)

nivel_inv_inicial = int(sys.argv[2])
num_meses = int(sys.argv[4])
num_policies = int(sys.argv[6])
num_valores_demanda = int(sys.argv[8])
media_intervalo_demanda = float(sys.argv[10])
costo_setup = float(sys.argv[12])
costo_incremental = float(sys.argv[14])
costo_mantenimiento = float(sys.argv[16])
costo_faltante = float(sys.argv[18])
minlag = float(sys.argv[20])
maxlag = float(sys.argv[22])
nro_corridas = int(sys.argv[24])


cantidad, bigs , nivel_inv, tipo_proximo_evento, num_eventos,  smalls = 0, 0, 0, 0, 0, 0
area_mantenimiento, area_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido = 0.0, 0.0, 0.0, 0.0, 0.0
prob_distrib_demanda = [0.0]*26
tiempo_proximo_evento = [0.0]*5

#-------------------------------------------------------------------------------------------------#
def random_integer(prob_distrib):
    u = random.random()
    for i in range(1, len(prob_distrib)):
        if u < prob_distrib[i]:
            return i
    return len(prob_distrib)

#-------------------------------------------------------------------------------------------------#
def inicializar():
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido
    global prob_distrib_demanda
    global tiempo_proximo_evento

    tiempo_simulacion = 0.0
    nivel_inv = nivel_inv_inicial
    tiempo_ultimo_evento = 0.0

    costo_total_pedido = 0.0
    area_mantenimiento = 0.0
    area_faltante = 0.0

    tiempo_proximo_evento[1] = 1.0e+30
    tiempo_proximo_evento[2] = tiempo_simulacion + random.expovariate(media_intervalo_demanda)
    tiempo_proximo_evento[3] = num_meses
    tiempo_proximo_evento[4] = 0.0

#-------------------------------------------------------------------------------------------------#
def temporizador():
    global tiempo_simulacion, tipo_proximo_evento
    global tiempo_proximo_evento
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
def llegada_pedido():
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido
    
    nivel_inv = nivel_inv + cantidad
    tiempo_proximo_evento[1] = 1.0e+30

#-------------------------------------------------------------------------------------------------#
def demanda():
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido

    nivel_inv = nivel_inv - random_integer(prob_distrib_demanda)

    tiempo_proximo_evento[2] = tiempo_simulacion + random.expovariate(media_intervalo_demanda) 

#-------------------------------------------------------------------------------------------------#
def evaluacion():
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido
    if(nivel_inv < smalls):
        cantidad = bigs - nivel_inv
        costo_total_pedido = costo_total_pedido + costo_setup + costo_incremental*cantidad

        tiempo_proximo_evento[1] = tiempo_simulacion + random.uniform(minlag, maxlag)
    
    tiempo_proximo_evento[4] = tiempo_simulacion + 1.0

#-------------------------------------------------------------------------------------------------#
def reporte(corrida):
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido

    costo_promedio_pedido = costo_total_pedido / num_meses
    costo_promedio_mantenimiento = costo_mantenimiento * area_mantenimiento / num_meses
    costo_promedio_faltante = costo_faltante * area_faltante / num_meses

    f.write("\nMaximo inventario: " + str(bigs) + "\n")
    f.write("\nMinimo inventario: " + str(smalls) + "\n")
    f.write("\nCorrida numero: "+str(corrida+1)+"\n")
    f.write("\nCosto total promedio: " + str(costo_promedio_faltante + costo_promedio_pedido + costo_promedio_mantenimiento) + "\n")
    f.write("\nCosto promedio de pedido: " + str(costo_promedio_pedido) + "\n")
    f.write("\nCosto promedio de mantenimiento: " + str(costo_promedio_mantenimiento) + "\n")
    f.write("\nCosto promedio de faltante: " + str(costo_promedio_faltante) + "\n")
    f.write("---------------------------------------------------------------------------")

#-------------------------------------------------------------------------------------------------#
def actualizacion_tiempo_prom_estadisticas():
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido
    tiempo_desde_ultimo_evento = tiempo_simulacion - tiempo_ultimo_evento
    tiempo_ultimo_evento = tiempo_simulacion

    if(nivel_inv < 0):
        area_faltante = area_faltante - nivel_inv * tiempo_desde_ultimo_evento
    elif(nivel_inv > 0):
        area_mantenimiento = area_mantenimiento + nivel_inv * tiempo_desde_ultimo_evento


#-------------------------------------------------------------------------------------------------#
num_eventos = 4

f=open("reporte.txt","w")

for x in range (num_valores_demanda):
    print("Ingrese el valor de probabilidad de demanda " + str(x + 1) + "\n")
    prob_distrib_demanda[x] = float(input())

f.write("Sistema de inventario de un solo producto\n\n")
f.write("Cantidad de inventario inicial: " + str(nivel_inv_inicial) + "\n\n")
f.write("Numero de tamaños de demanda: " + str(num_valores_demanda) + "\n\n")
f.write("Distribucion de tamaños de demanda: " + str(prob_distrib_demanda) + "\n\n")
f.write("Media de intervalo de demanda: " + str(media_intervalo_demanda) + "\n\n")
f.write("Demora de envio de " + str(minlag) + " a " + str(maxlag) + " meses\n\n")
f.write("Largo de la simulacion: " + str(num_meses) + " meses\n\n")
f.write("K= " + str(costo_setup) + " i= " +str(costo_incremental)+ " h= " +str(costo_mantenimiento)+" pi= "+str(costo_faltante)+ "\n\n")
f.write("Numero de politicas: " + str(num_policies) + "\n\n")
f.write("---------------------------------------------------------------------------")

for x in range(num_policies):
    eje_x = []
    eje_y_inv = []
    eje_y_inv_pos = []
    eje_y_inv_neg = []
    referencia = []
    print("Ingrese el valor de smalls: \n")
    smalls = int(input())
    print("Ingrese el valor de bigs: \n")
    bigs = int(input())

    for i in range(nro_corridas):
        inicializar()
        eje_x = []
        eje_y_inv = []
        eje_y_inv_pos = []
        eje_y_inv_neg = []
        referencia = []
        plt.figure(1)
        plt.figure(2)
        plt.figure(3)
        while True:
            temporizador()
            actualizacion_tiempo_prom_estadisticas()
            if(tipo_proximo_evento == 1):
                llegada_pedido()
            elif(tipo_proximo_evento == 2):
                demanda()
            elif(tipo_proximo_evento == 4):
                evaluacion()
            elif(tipo_proximo_evento == 3):
                reporte(i)
            
            eje_x.append(tiempo_simulacion)
            eje_y_inv.append(nivel_inv)
            eje_y_inv_pos.append(max(nivel_inv,0))
            eje_y_inv_neg.append(max(nivel_inv*(-1), 0))
            referencia.append(0)

            if(tipo_proximo_evento == 3):
                break
        
        plt.figure(1)
        plt.step(eje_x, eje_y_inv, color = "red", label = "I")
        plt.plot(eje_x,referencia,color = "black", linestyle='dashed')
        plt.legend()
        plt.savefig("Graficas/nivel_inventario_politica_("+str(smalls)+", "+str(bigs)+")_corrida_"+str(i)+".jpg")
        plt.clf()

        plt.figure(2)
        plt.plot(eje_x,referencia,color = "black", linestyle='dashed')
        plt.step(eje_x, eje_y_inv_neg, color = "blue", label = "I-")
        plt.legend()
        plt.savefig("Graficas/nivel_inventarioNeg_politica_("+str(smalls)+", "+str(bigs)+")_corrida_"+str(i)+".jpg")
        plt.clf()

        plt.figure(3)
        plt.plot(eje_x,referencia,color = "black", linestyle='dashed')
        plt.step(eje_x, eje_y_inv_pos, color = "green", label = "I+")
        plt.legend()
        plt.savefig("Graficas/nivel_inventarioPos_politica_("+str(smalls)+", "+str(bigs)+")_corrida_"+str(i)+".jpg")
        plt.clf()

  
f.close()

