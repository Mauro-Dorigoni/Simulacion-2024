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
    return (math.round(var_esp)),desv_esp

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
if len(sys.argv)!=5 or sys.argv[1]!="-c" or sys.argv[3]!="-n":
    print("Uso: python sim_ruleta.py -c <nro_iteraciones> -n <nro_elegido>")
    sys.exit(1)

#Obtengo el nro de iteraciones y el nro elegido de la CLI#
nro_iteraciones=int(sys.argv[2])
nro_elegido=int(sys.argv[4])


#Empiezo con grafica frecuencia vs iteracion#
valores=[0 for x in range (nro_iteraciones)]
frec_rel_real_grafica=[0.000 for x in range(nro_iteraciones)]
for index in range(len(valores)):
    valores[index]=int(random.randint(0,36))
    frec_abs,frec_rel=calculo_frecuencias(valores,nro_elegido)
    frec_rel_real_grafica[index]=frec_rel
frec_rel_esperada_grafica=[(1/37) for x in range(nro_iteraciones)]
nro_tiradas=[0 for x in range(nro_iteraciones)]
for index in range (len(nro_tiradas)):
    nro_tiradas[index]=index
plt.plot(nro_tiradas,frec_rel_real_grafica)
plt.title('Frecuencia relativa vs numero de tiradas')
plt.xlabel('numero tiradas')
plt.ylabel('frecuencia relativa')
plt.show()