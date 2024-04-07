import random
import array as arr
import statistics
import math
import sys
import matplotlib as plt
import matplotlib.pyplot as plt

#Funcion calculo de promedio esperado#
def calculo_promedio_esperado():
    return 18;

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
def calculo_var_desv_reales(valores,prom_real):
    var_real=0
    desv_real=0
    for x in range(37):
        frec_abs,frec_rel=calculo_frecuencias(valores,x)
        var_real=var_real + (((x-prom_real)**2)*frec_rel)
    desv_real=math.sqrt(var_real)
    return var_real,desv_real

#compurebo que el programa en CLI se use como se debe#
if len(sys.argv)!=7 or sys.argv[1]!="-c" or sys.argv[3]!="-n" or sys.argv[5]!="-e":
    print("Uso: python sim_ruleta.py -c <nro_corridas> -n <nro_iteraciones> -e <nro_elegido>")
    sys.exit(1)

#Obtengo el nro de iteraciones y el nro elegido de la CLI#
nro_corridas=int(sys.argv[2])
nro_iteraciones=int(sys.argv[4])
nro_elegido=int(sys.argv[6])


#Programa Principal#
#Eje x en graficas por corrida#
nro_corridas_eje_x=[0 for x in range(nro_corridas)]
for index in range(nro_corridas):
    nro_corridas_eje_x[index]=index

#Declaracion de ejes y en graficas con corridas en el eje x#
frec_rel_prom_p_corrida=[0.000 for x in range(nro_corridas)]
valor_prom_prom_p_corrida=[0.000 for x in range(nro_corridas)]
var_prom_p_corrida=[0.000 for x in range(nro_corridas)]
desv_prom_p_corrida=[0.000 for x in range(nro_corridas)]

for j in range (nro_corridas): #El for para cada corrida#
    valores=[0 for x in range (nro_iteraciones)]

    #Declaracion de ejes y en graficas con tiradas en el eje x#
    frec_rel_real_grafica=[0.000 for x in range(nro_iteraciones)]
    valor_prom_p_tirada=[0.000 for x in range(nro_iteraciones)]
    var_p_tirada=[0.000 for x in range(nro_iteraciones)]
    desv_p_tirada=[0.000 for x in range(nro_iteraciones)]

    for index in range(len(valores)): #El for para cada tirada#
        valores[index]=int(random.randint(0,36))
        #Calculo eje y en grafica frecuencia por tirada#
        frec_abs,frec_rel=calculo_frecuencias(valores,nro_elegido)
        frec_rel_real_grafica[index]=frec_rel
        #Calculo eje y en grafica valor promedio por tirada#
        valor_prom_p_tirada[index]=statistics.mean(valores)
        var_real,desv_real=calculo_var_desv_reales(valores,valor_prom_p_tirada[index])
        #Calculo eje y en grafica varianza por tirada#
        var_p_tirada[index]=var_real
        #Calculo eje y grafica desvio por tirada#
        desv_p_tirada[index]=desv_real
    
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

    #Graficas de Tiradas#
    if(j==0):
        f=plt.figure(1)
        plt.plot(nro_tiradas,frec_rel_real_grafica, label='frn',color='red')
        plt.plot(nro_tiradas,frec_rel_esperada_grafica,label='fre', color='blue')
        plt.title('Frecuencia relativa (real y esperada) vs numero de tiradas')
        plt.xlabel('numero tiradas')
        plt.ylabel('frecuencia relativa')
        plt.legend()
        f.savefig('grafica_frecuencia_por_tirada.png')
        p=plt.figure(2)
        plt.plot(nro_tiradas,valor_prom_p_tirada, label='vpn',color='red')
        plt.plot(nro_tiradas,prom_esperado_tirada_grafica,label='vpe', color='blue')
        plt.title('Valor promedio (real y esperado) vs numero de tiradas')
        plt.xlabel('numero tiradas')
        plt.ylabel('Valor promedio')
        plt.legend()
        p.savefig('grafica_promedio_por_tirada.png')
        d=plt.figure(3)
        plt.plot(nro_tiradas,desv_p_tirada, label='vd',color='red')
        plt.plot(nro_tiradas,desv_esperad0_tirada_grafica,label='vde', color='blue')
        plt.title('Desvio (real y esperado) vs numero de tiradas')
        plt.xlabel('numero tiradas')
        plt.ylabel('Desvio')
        plt.legend()
        d.savefig('grafica_desvio_por_tirada.png')
        v=plt.figure(4)
        plt.plot(nro_tiradas,var_p_tirada, label='vvn',color='red')
        plt.plot(nro_tiradas,var_esperada_tirada_grafica,label='vve', color='blue')
        plt.title('Varianza (real y esperada) vs numero de tiradas')
        plt.xlabel('numero tiradas')
        plt.ylabel('Varianza')
        plt.legend()
        v.savefig('grafica_varianza_por_tirada.png')
    
    #Calculo eje y en grafica frecuencia promedio por corrida#
    frec_rel_prom_p_corrida[j]=statistics.mean(frec_rel_real_grafica)
    #Calculo eje y en grafica valor promedio promedio por corrida#
    valor_prom_prom_p_corrida[j]=statistics.mean(valor_prom_p_tirada)
    #Calculo eje y en grafica varianza promedio por corrida#
    var_prom_p_corrida[j]=statistics.mean(var_p_tirada)
    #Calculo eje y en grafica desvio promedio por corrida#
    desv_prom_p_corrida[j]=statistics.mean(desv_p_tirada)

#Valores esperados promedio por corrida#
frec_rel_prom_esp_p_corrida=[(1/37) for x in range(nro_corridas)]
prom_prom_esp_p_corrida=[18 for x in range(nro_corridas)]
var_esp,desv_esp=calculo_var_desv_esperados()
var_prom_esp_p_corrida=[var_esp for x in range(nro_corridas)]
desv_prom_esp_p_corrida=[desv_esp for x in range(nro_corridas)]

#Graficas por corridas#
fp=plt.figure(5)
plt.plot(nro_corridas_eje_x,frec_rel_prom_p_corrida, label='fprn',color='red')
plt.plot(nro_corridas_eje_x,frec_rel_prom_esp_p_corrida,label='fpre', color='blue')
plt.title('Frecuencia relativa promedio (real y esperada) vs numero de corridas')
plt.xlabel('numero corridas')
plt.ylabel('frecuencia relativa promedio')
plt.legend()
fp.savefig('frecuencia_promedio_corrida.png')
vpp=plt.figure(6)
plt.plot(nro_corridas_eje_x,valor_prom_prom_p_corrida, label='vppn',color='red')
plt.plot(nro_corridas_eje_x,prom_prom_esp_p_corrida,label='vppe', color='blue')
plt.title('Valor promedio promedio (real y esperado) vs numero de corridas')
plt.xlabel('numero corridas')
plt.ylabel('Valor promedio promedio')
plt.legend()
vpp.savefig('valor_promedio_promedio_corrida.png')
dp=plt.figure(7)
plt.plot(nro_corridas_eje_x,desv_prom_p_corrida, label='vdp',color='red')
plt.plot(nro_corridas_eje_x,desv_prom_esp_p_corrida,label='vdpe', color='blue')
plt.title('Desvio promedio (real y esperado) vs numero de corridas')
plt.xlabel('numero corridas')
plt.ylabel('Desvio promedio')
plt.legend()
dp.savefig('desvio_promedio_corrida.png')
vp=plt.figure(8)
plt.plot(nro_corridas_eje_x,var_prom_p_corrida, label='vvpn',color='red')
plt.plot(nro_corridas_eje_x,var_prom_esp_p_corrida,label='vvpe', color='blue')
plt.title('Varianza promedio (real y esperada) vs numero de corridas')
plt.xlabel('numero corridas')
plt.ylabel('Varianza promedio')
plt.legend()
vp.savefig('varianza_promedio_corrida.png')