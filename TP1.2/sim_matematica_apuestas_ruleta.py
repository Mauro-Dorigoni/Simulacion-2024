import random
import array as arr
import statistics
import math
import sys
import matplotlib as mpl
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
banca=10

#Funcion para graficar el flujo de caja en 1 corrida#
def graph_flujo_caja(flujo_caja,corrida_actual,estrategia):
    nro_tiradas_eje_x=[x for x in range(len(flujo_caja))]
    f=plt.figure()
    plt.plot(nro_tiradas_eje_x,flujo_caja,label="fc",color="red")
    if tipo_capital=="f":
        plt.axhline(y=banca, color='b', linestyle='-')
    plt.xlabel("numero de tiradas") 
    plt.ylabel("cantidad de capital") 
    plt.title("grafica_flujo_caja_corrida"+str(corrida_actual)+"_para_"+estrategia)
    plt.legend()
    f.savefig("grafica_flujo_caja_corrida"+str(corrida_actual)+"_para_"+estrategia+".jpg")

def graph_resumen_corridas(datos,estrategia):
    mpl.style.use("default")
    nro_tiradas_eje_x=[x for x in range(nro_iteraciones+1)]
    f=plt.figure()
    for x in range (len(datos)):
        plt.plot(nro_tiradas_eje_x[:len(datos[x])],datos[x],label="fc"+str(x),color="C"+str(x%10+1))
    if tipo_capital=="f":
        plt.axhline(y=banca, color='b', linestyle='-')
    plt.xlabel("numero de tiradas") 
    plt.ylabel("cantidad de capital") 
    plt.title("grafica_resumen_corridas_para_"+estrategia)
    plt.legend()
    f.savefig("grafica_resumen_corridas_para_"+estrategia+".jpg")

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
def martingala(nro_tiradas,tipo_capital,banca,corrida_actual):
    flujo_caja=[0 for x in range(nro_tiradas+1)]
    paso_a_usar=1
    apuesta=1
    ejex=(nro_tiradas+1)
    if tipo_capital=="f":
        flujo_caja[0]=banca
        ganancias=banca
        for x in range (nro_tiradas):
            if ganancias<=0 or apuesta>ganancias: break
            salida=int(random.randint(0,36))
            paso_a_usar,ganancias,apuesta=martingala_sig_paso(apuesta,paso_a_usar,ganancias,salida) 
            flujo_caja[x+1]=ganancias
            ejex=x+2

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            paso_a_usar,ganancias,apuesta=martingala_sig_paso(apuesta,paso_a_usar,ganancias,salida) 
            flujo_caja[x+1]=ganancias
    graph_flujo_caja(flujo_caja[:ejex],corrida_actual,"martingala")
    return (flujo_caja[:ejex])

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
def dalambert(nro_tiradas,tipo_capital,banca,corrida_actual):
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
            ejex=x+2

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            ganancias,apuesta=dalambert_sig_paso(apuesta,ganancias,salida) 
            flujo_caja[x+1]=ganancias
    graph_flujo_caja(flujo_caja[:ejex],corrida_actual,"dalambert")
    return (flujo_caja[:ejex])


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
def fibonacci(nro_tiradas,tipo_capital,banca,corrida_actual):
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
            ejex=x+2

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            ganancias,apuesta=fibonacci_sig_paso(apuesta,ganancias,salida)
            flujo_caja[x+1]=ganancias
    graph_flujo_caja(flujo_caja[:ejex],corrida_actual,"fibonacci")
    return (flujo_caja[:ejex])
#Estrategia propia siguiente paso#
def proporcion_constante_sig_paso(apuesta,ganancias,salida,nro_elegido):
    if salida==nro_elegido:
        ganancias=ganancias+apuesta*36
    else:
        ganancias=ganancias-apuesta

    if ganancias<10 and ganancias>-10:
        apuesta=1
    else:
        apuesta=abs(round(ganancias*0.1))

    return ganancias,apuesta

#Estrategia propia#
def proporcion_constante(nro_tiradas,tipo_capital,nro_elegido,banca,corrida_actual):
    flujo_caja=[0 for x in range(nro_tiradas+1)]
    ejex=nro_tiradas
    if tipo_capital=="f":
        apuesta=round(banca*0.1)
        ganancias=banca
        flujo_caja[0]=banca
        for x in range (nro_tiradas):
            if ganancias<=0 or apuesta>ganancias: break
            salida=int(random.randint(0,36))
            ganancias,apuesta=proporcion_constante_sig_paso(apuesta,ganancias,salida,nro_elegido) 
            flujo_caja[x+1]=ganancias
            ejex=x+2

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        apuesta=1
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            ganancias,apuesta=proporcion_constante_sig_paso(apuesta,ganancias,salida,nro_elegido) 
            flujo_caja[x+1]=ganancias
    graph_flujo_caja(flujo_caja[:ejex],corrida_actual,"prop_constante")
    return (flujo_caja[:ejex])

def nosabemos(estrategia):
    datos=[[0 for x in range(nro_iteraciones+1)] for f in range(nro_corridas)]
    for x in range(nro_corridas):
        if estrategia=="m":
            datos[x]=martingala(nro_iteraciones,tipo_capital,10,x)
        elif estrategia=="d":
            datos[x]=dalambert(nro_iteraciones,tipo_capital,10,x)
        elif estrategia=="f":
            datos[x]=fibonacci(nro_iteraciones,tipo_capital,10,x)
        elif estrategia=="o":
            datos[x]=proporcion_constante(nro_iteraciones,tipo_capital,nro_elegido,10,x)
        else: 
            print("algo salio mal")
    graph_resumen_corridas(datos,estrategia)



#Programa Principal#
print("qcyo")
nosabemos(estrategia)

