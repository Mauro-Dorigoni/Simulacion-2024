import random
from PIL import Image
import array as arr
import statistics
import sys
import math
import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.stats import binom,kstest,norm
import numpy as np


#compurebo que el programa en CLI se use como se debe#
if len(sys.argv)!=5 or sys.argv[1]!="-s" or sys.argv[3]!="-n":
    print("Uso: python numeros_psa.py -s <semilla> -n <nro_iteraciones>")
    sys.exit(1)
semilla_inicial=int(sys.argv[2])
corridas=int(sys.argv[4])
sem_ini=str(semilla_inicial)

def bitmap(resultados,metodo,semilla):
    x=0
    y=0
    tam=int(math.sqrt(len(resultados)))
    img = Image.new( 'RGB', (tam,tam), "black")
    pixels = img.load()
    for i in range(len(resultados)):
        aux=str(resultados[i])
        prueba=int(aux[2])
        if(prueba % 2 == 0):
            pixels[x,y] = (255,255,255)
        if(y+1>=512):
            y=0
            x=x+1
        else: y=y+1
    img.save('bitmap_'+metodo+'_semilla_'+semilla+'.png')


def glc(semilla):
    a = 1664525
    c = 1013904223
    m = 2**32
    subtotal = semilla * a + c
    pseudoaleatorio = subtotal % m
    random = pseudoaleatorio / (m - 1)
    return random

def vonNewman (semilla):
    s_str=str(semilla*semilla)
    while len(s_str)!=10:
        s_str="0"+s_str
    n_rand=(int(s_str[2:6]))
    return n_rand


def merseneTwister(semilla):
    random.seed(semilla)
    return random.random()

def prueba_bondad_ajuste(resultados,metodo):
    intervalos=10
    frecuenciua_absoluta=[0 for x in range(10)]
    frec_esperada=len(resultados)/10
    k_crit=16.92
    x_sqr=0.0
    for i in range (len(resultados)):
        if(resultados[i]>=0.0 and resultados[i]<0.1):
            frecuenciua_absoluta[0]=frecuenciua_absoluta[0]+1
        elif(resultados[i]>=0.1 and resultados[i]<0.2):
            frecuenciua_absoluta[1]=frecuenciua_absoluta[1]+1
        elif(resultados[i]>=0.2 and resultados[i]<0.3):
            frecuenciua_absoluta[2]=frecuenciua_absoluta[2]+1
        elif(resultados[i]>=0.3 and resultados[i]<0.4):
            frecuenciua_absoluta[3]=frecuenciua_absoluta[3]+1
        elif(resultados[i]>=0.4 and resultados[i]<0.5):
            frecuenciua_absoluta[4]=frecuenciua_absoluta[4]+1
        elif(resultados[i]>=0.5 and resultados[i]<0.6):
            frecuenciua_absoluta[5]=frecuenciua_absoluta[5]+1
        elif(resultados[i]>=0.6 and resultados[i]<0.7):
            frecuenciua_absoluta[6]=frecuenciua_absoluta[6]+1
        elif(resultados[i]>=0.7 and resultados[i]<0.8):
            frecuenciua_absoluta[7]=frecuenciua_absoluta[7]+1
        elif(resultados[i]>=0.8 and resultados[i]<0.9):
            frecuenciua_absoluta[8]=frecuenciua_absoluta[8]+1
        elif(resultados[i]>=0.9 and resultados[i]<1.0):
            frecuenciua_absoluta[9]=frecuenciua_absoluta[9]+1
    
    for j in range(10):
        x_sqr=x_sqr+(((frecuenciua_absoluta[j]-frec_esperada)**2)/frec_esperada)
    
    if(x_sqr>k_crit):
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" no pasa la prueba de chi cuadrado\n")
        f.close()
    else:
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" pasa la prueba de chi cuadrado\n")
        f.close()


def corridas_mediana(resultados, metodo):
    mediana=statistics.median(resultados)
    mediana_linea=[mediana for x in range(len(resultados))]
    raobm=["x" for x in range(len(resultados))]
    eje_x=[x for x in range(len(resultados))]
    corridas=1
    for i in range(len(resultados)):
        if(resultados[i]>mediana):
            raobm[i]="a"
        elif(resultados[i]<mediana):
            raobm[i]="b"
    
    for x in range(1,(len(raobm))):
        if(raobm[x]!=raobm[x - 1]):
            corridas=corridas+1
    n1=raobm.count("a")
    n2=raobm.count("b")
    corridas_esperadas=((2 * n1 * n2) / (n1 + n2)) + 1
    std_dev=np.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / ((n1 + n2) ** 2 * (n1 + n2 - 1)))
    if(std_dev==0):
        std_dev=semilla_inicial
    z=(corridas-corridas_esperadas)/std_dev
    p_value = 2 * (1 - norm.cdf(abs(z)))
    if(p_value<0.05):
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" no pasa la prueba de corridaS\n")
        f.close()
    else:
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" pasa la prueba de corridas\n")
        f.close()


def sumas_superpuestas(resultados,metodo):
    m=512
    n=len(resultados)
    sumas=[sum(resultados[i:i+m]) for i in range(n - m + 1)]
    mean_sum = np.mean(sumas)
    std_sum = np.std(sumas)
    normalized_sums = [(x - mean_sum) / std_sum for x in sumas]
    ks_statistic, p_value = kstest(normalized_sums, 'norm')
    if(p_value<0.05):
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" no pasa la prueba de sumas superpuestas\n")
        f.close()
    else:
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" pasa la prueba de sumas superpuestas\n")
        f.close()

def reverse_arrangements(resultados,metodo):
    N = len(resultados)
    ascending_pairs = 0
    descending_pairs = 0
    for i in range(N - 1):
        if resultados[i] < resultados[i + 1]:
            ascending_pairs += 1
        elif resultados[i] > resultados[i + 1]:
            descending_pairs += 1
    total_pairs = N - 1
    expected_pairs = total_pairs / 2
    observed_ratio = ascending_pairs / total_pairs
    p_value = 1 - binom.cdf(ascending_pairs, total_pairs, 0.5)
    if(p_value<0.05):
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" no pasa la prueba de reverse arrangements\n")
        f.close()
    else:
        f=open("resultados.txt","a")
        f.write("El metodo "+metodo+" pasa la prueba de reverse arrangements\n")
        f.close()


resultados=[(0.0000) for x in range(corridas)]
m = 2**32
semilla = glc(semilla_inicial)
for x in range(corridas):
    resultados[x]=semilla
    semilla=glc(semilla*(m -1))
bitmap(resultados,'glc',sem_ini)
prueba_bondad_ajuste(resultados,'glc')
corridas_mediana(resultados,"glc")
sumas_superpuestas(resultados,"glc")
reverse_arrangements(resultados,"glc")


resultados=[(0.0000) for x in range(corridas)]
semilla=semilla_inicial
for x in range(corridas):
    semilla=merseneTwister(semilla)
    resultados[x]=semilla
bitmap(resultados,'mt',sem_ini)
prueba_bondad_ajuste(resultados,'mt')
corridas_mediana(resultados,"mt")
sumas_superpuestas(resultados,"mt")
reverse_arrangements(resultados,"mt")

resultados=[(0.0000) for x in range(corridas)]
semilla=semilla_inicial
for x in range(corridas):
    semilla=vonNewman(semilla)
    resultados[x]=semilla/10000
bitmap(resultados,'vn',sem_ini)
prueba_bondad_ajuste(resultados,'vonNewman')
corridas_mediana(resultados,"vonNewman")
sumas_superpuestas(resultados,"vonNewman")
reverse_arrangements(resultados,"vonNewman")

