import random
import array as arr
import statistics
import math
import sys
import matplotlib as plt
import matplotlib.pyplot as plt

"""#Funcion calculo de promedio esperado#
def calculo_promedio_esperado():
    return 18

#Funcion calculo de Varianza y Desvio esperados#
def calculo_var_desv_esperados():
    var_esp=0
    desv_esp=0
    for x in range(37):
        var_esp=var_esp+(((x-18)**2)*(1/37))
    desv_esp=math.sqrt(var_esp)
    return var_esp,desv_esp

#Funcion calculo frecuencias esperadas#
def calculo_frec_esperadas (nro_iteraciones):
    return (nro_iteraciones/37)

#Funcion calculo de frecuencias#
def calculo_frecuencias (valores, nro_elegido):
    frec_abs = valores.count(nro_elegido)
    frec_rel = frec_abs/len(valores)
    return frec_abs, frec_rel

#Funcion calculo promedio real#
def calculo_promedio_real(valores):
    return statistics.mean(valores)

#Funcion calculo varianza y desvio reales#
def calculo_var_desv_reales(valores):
    var_real=0
    desv_real=0
    prom_real=statistics.mean(valores)
    for x in range(37):
        frec_abs,frec_rel=calculo_frecuencias(valores,x)
        var_real=var_real + (((x-prom_real)**2)*frec_rel)
    desv_real=math.sqrt(var_real)
    return var_real,desv_real """

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

def graph_flujo_caja(flujo_caja):
    nro_tiradas_eje_x=[x for x in range(len(flujo_caja))]
    #print(flujo_caja, nro_tiradas_eje_x)
    f=plt.figure()
    plt.plot(nro_tiradas_eje_x,flujo_caja,label="fc",color="red")
    plt.legend()
    f.savefig("prueba.jpg")


def martingala_sig_paso(apuesta,paso,ganancias,salida):
    negro=[15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26]
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

def martingala(nro_tiradas,tipo_capital,banca):
    flujo_caja=[0 for x in range(nro_tiradas+1)]
    paso_a_usar=1
    apuesta=1
    ejex=nro_tiradas
    if tipo_capital=="f":
        flujo_caja[0]=banca
        ganancias=banca
        for x in range (nro_tiradas):
            if ganancias<=0: break
            salida=int(random.randint(0,36))
            paso_a_usar,ganancias,apuesta=martingala_sig_paso(apuesta,paso_a_usar,ganancias,salida) 
            flujo_caja[x+1]=ganancias
            ejex=x+1
            print(ejex)

    if tipo_capital=="i":
        flujo_caja[0]=0
        ganancias=0
        for x in range (nro_tiradas):
            salida=int(random.randint(0,36))
            paso_a_usar,ganancias,apuesta=martingala_sig_paso(apuesta,paso_a_usar,ganancias,salida) 
            flujo_caja[x+1]=ganancias
    print(flujo_caja)
    graph_flujo_caja(flujo_caja[:(ejex+1)])



#def dalambert(nro_tiradas, tipo_capital,banca):



#Programa Principal#
martingala(nro_iteraciones,tipo_capital,10)
print("qcyo")



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
    