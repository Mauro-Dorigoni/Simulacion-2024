import random
import array as arr
import statistics
import math
import sys
import matplotlib as plt
import matplotlib.pyplot as plt

negro=[15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26]

#compurebo que el programa en CLI se use como se debe#
if  (len(sys.argv)!=11) or sys.argv[1]!="-c" or sys.argv[3]!="-n" or sys.argv[5]!="-e" or sys.argv[7]!="-s" or sys.argv[9]!="-a" or (sys.argv[8] not in ["m","d","f","o"]) or (sys.argv[10] not in ["i","f"]):
    print("Uso: python sim_matematica_apuestas_ruleta.py -c <nro_corridas> -n <nro_iteraciones> -e <nro_elegido> -s <estrategia [m|d|f|o]> -a <tipo_capital [i|f]>")
    sys.exit(1)

#Obtengo el nro de iteraciones y el nro elegido de la CLI#
nro_corridas=int(sys.argv[2])
nro_iteraciones=int(sys.argv[4])
nro_elegido=int(sys.argv[6])
estrategia=(sys.argv[8])
tipo_capital=(sys.argv[10])

#Funcion para graficar el flujo de caja en 1 corrida#
def graph_flujo_caja(flujo_caja):
    nro_tiradas_eje_x=[x for x in range(len(flujo_caja))]
    f=plt.figure()
    plt.plot(nro_tiradas_eje_x,flujo_caja,label="fc",color="red")
    plt.legend()
    f.savefig("prueba.jpg")

#Funcion para determinar el siguiente paso a tomar en estrategia martingala#
def martingala_sig_paso(apuesta,paso,ganancias,salida):
    if salida in negro:
        ganancias=ganancias+apuesta*2
        apuesta=1
        return 1,ganancias,apuesta
    else:
        ganancias=ganancias-apuesta
        apuesta=apuesta*2
        if paso==5:
            apuesta=1 
            return 1,ganancias,apuesta
        return paso+1,ganancias,apuesta

#Funcion que llama a la estrategia martingala#
def martingala(nro_tiradas,tipo_capital,banca):
    flujo_caja=[0 for x in range(nro_tiradas+1)]
    paso_a_usar=1
    apuesta=1
    ejex=nro_tiradas
    if tipo_capital=="f":
        flujo_caja[0]=banca
        ganancias=banca
        for x in range (nro_tiradas):
            if ganancias<=0 or apuesta>ganancias: break
            salida=int(random.randint(0,36))
            paso_a_usar,ganancias,apuesta=martingala_sig_paso(apuesta,paso_a_usar,ganancias,salida) 
            flujo_caja[x+1]=ganancias
            ejex=x+1

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            paso_a_usar,ganancias,apuesta=martingala_sig_paso(apuesta,paso_a_usar,ganancias,salida) 
            flujo_caja[x+1]=ganancias
    graph_flujo_caja(flujo_caja[:(ejex+1)])

#Funcion para determinar el siguiente paso a tomar en estrategia dalambert#
def dalambert_sig_paso(apuesta,ganancias,salida):
    if salida in negro:
        ganancias=ganancias+apuesta*2
        if apuesta==1:
            return ganancias,1
        else:
            return ganancias,apuesta-1
    else:
        ganancias=ganancias-apuesta
        return ganancias,apuesta+1

#Funcion que llama a la estrategia dalambert#
def dalambert(nro_tiradas,tipo_capital,banca):
    apuesta=1
    flujo_caja=[0 for x in range(nro_tiradas+1)]
    ejex=nro_tiradas
    if tipo_capital=="f":
        ganancias=banca
        flujo_caja[0]=banca
        for x in range (nro_tiradas):
            if ganancias<=0 or apuesta>ganancias: break
            salida=int(random.randint(0,36))
            ganancias,apuesta=dalambert_sig_paso(apuesta,ganancias,salida) 
            flujo_caja[x+1]=ganancias
            ejex=x+1

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            ganancias,apuesta=dalambert_sig_paso(apuesta,ganancias,salida) 
            flujo_caja[x+1]=ganancias
    graph_flujo_caja(flujo_caja[:(ejex+1)])


#Funcion para determinar el siguiente paso a tomar en estrategia fibonacci#
def fibonacci_sig_paso(apuesta,ganancias,salida):
    apuesta_previa,apuesta_curr=apuesta
    if salida in negro:
        ganancias=ganancias+apuesta_curr*2
        if (apuesta==[1,1]):
            return ganancias,[1,1]
        if (apuesta==[1,2]):
            return ganancias,[1,1]
        else:
            nueva_apuesta=apuesta_curr-apuesta_previa
            return ganancias,[apuesta_previa-nueva_apuesta,nueva_apuesta]
    else:
        ganancias=ganancias-apuesta_curr
        return ganancias,[apuesta_curr,apuesta_previa+apuesta_curr]

#Funcion que llama a la estrategia fibonacci#
def fibonacci(nro_tiradas,tipo_capital,banca):
    apuesta=[1,1]
    flujo_caja=[0 for x in range(nro_tiradas+1)]
    ejex=nro_tiradas
    if tipo_capital=="f":
        ganancias=banca
        flujo_caja[0]=banca
        for x in range (nro_tiradas):
            if ganancias<=0 or apuesta[1]>ganancias: break
            salida=int(random.randint(0,36))
            ganancias,apuesta=fibonacci_sig_paso(apuesta,ganancias,salida)
            flujo_caja[x+1]=ganancias
            ejex=x+1

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            print(apuesta)
            ganancias,apuesta=fibonacci_sig_paso(apuesta,ganancias,salida)
            flujo_caja[x+1]=ganancias
    print(flujo_caja)
    graph_flujo_caja(flujo_caja[:(ejex+1)])

#Programa Principal#
print("qcyo")
dalambert(nro_iteraciones,tipo_capital,10)


""" #Programa Principal#
#Eje x en graficas por corrida#
nro_corridas_eje_x=[0 for x in range(nro_corridas)]
for index in range(nro_corridas):
    nro_corridas_eje_x[index]=index

#Declaracion de ejes y en graficas con corridas en el eje x#
curva_frec_rel_p_corrida=[[0.000 for x in range(nro_iteraciones)] for f in range(nro_corridas)]
curvas_valor_prom_p_corrida=[[0.000 for x in range(nro_iteraciones)] for f in range(nro_corridas)]
curvas_var_p_corrida=[[0.000 for x in range(nro_iteraciones)] for f in range(nro_corridas)]
curvas_desv_prom_p_corrida=[[0.000 for x in range(nro_iteraciones)] for f in range(nro_corridas)]

for j in range (nro_corridas): #El for para cada corrida#
    valores=[0 for x in range (nro_iteraciones)]


    for index in range(len(valores)): #El for para cada tirada#
        valores[index]=int(random.randint(0,36))
        #Calculo eje y en grafica frecuencia por tirada#
        frec_abs,frec_rel=calculo_frecuencias(valores,nro_elegido)
        curva_frec_rel_p_corrida[j][index]=frec_rel
        #Calculo eje y en grafica valor promedio por tirada#
        curvas_valor_prom_p_corrida[j][index]=statistics.mean(valores)
        var_real,desv_real=calculo_var_desv_reales(valores)
        #Calculo eje y en grafica varianza por tirada#
        curvas_var_p_corrida[j][index]=var_real
        #Calculo eje y grafica desvio por tirada#
        curvas_desv_prom_p_corrida[j][index]=desv_real
    
    #Valores esperados por tirada#
    frec_rel_esperada_grafica=[(1/37) for x in range(nro_iteraciones)]
    prom_esperado_tirada_grafica=[(calculo_promedio_esperado()) for x in range(nro_iteraciones)]
    var_esp,dev_esp=calculo_var_desv_esperados()
    var_esperada_tirada_grafica=[var_esp for x in range(nro_iteraciones)]
    desv_esperad0_tirada_grafica=[dev_esp for x in range(nro_iteraciones)]


    
#Eje x en Graficas por tirada#
nro_tiradas=[0 for x in range(nro_iteraciones)]
for index in range (len(nro_tiradas)):
    nro_tiradas[index]=index    


#Valores esperados promedio por corrida#
frec_rel_prom_esp_p_corrida=[(1/37) for x in range(nro_iteraciones)]
prom_prom_esp_p_corrida=[18 for x in range(nro_iteraciones)]
var_esp,desv_esp=calculo_var_desv_esperados()
var_prom_esp_p_corrida=[var_esp for x in range(nro_iteraciones)]
desv_prom_esp_p_corrida=[desv_esp for x in range(nro_iteraciones)] """
    