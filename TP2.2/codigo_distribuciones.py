import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

#Definicion de variables necesarias#
inferior=1
superior=10
n=100
lambde=0.7
alfa=1
beta=2
mu=55
sigma=6
n1 = 5 
p = 0.3
M = 20  
n2 = 7 
N = 5 
lam = 5
val = [1, 2, 3, 4, 5]
prob = [0.1, 0.2, 0.3, 0.2, 0.2]

#Generacion de un numero con distribucion uniforme - metodo mersenne-twister#
def numero_dist_uniforme(inferior, superior):
    return random.uniform(inferior, superior)

#Generacion de un numero con distribucion exponencial - metodo mersenne-twister#
def numero_dist_exponencial(lambde):
    return random.expovariate(lambde)

#Generacion de un numero con distribucion gamma - metodo mersenne-twister#
def numero_dist_gamma(alfa,beta):
    return random.gammavariate(alfa,beta)

#Generacion de un numero con distribucion normal - metodo mersenne-twister#
def numero_dist_normal(mu,sigma):
    return random.normalvariate(mu,sigma)

#Generacion de un numero con distribucion pascal#
def numero_dist_pascal(n,p):
    return stats.nbinom.rvs(n,p)

#Generacion de un numero con distribucion binomial#
def numero_dist_binomial(n,p):
    return stats.binom.rvs(n,p)

#Generacion de un numero con distribucion hipergeometrica#
def numero_dist_hipergeometrica(M,n,N):
    return stats.hypergeom.rvs(n,p)

#Generacion de un numero con distribucion poisson#
def numero_dist_poisson(lam):
    return stats.poisson.rvs(lam)

#Generacion de un numero con distribucion empirica discreta#
def numero_dist_ed(val,prob):
    return np.random.choice(val, p=prob)


#Generacion de n numeros uniformes (ingreso en llamada al programa)#
def dist_uniforme(n):
    numeros_dist_uniforme=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_uniforme[x]=numero_dist_uniforme(inferior,superior)
    return(numeros_dist_uniforme)

#Generacion de n numeros exponenciales (ingreso en llamada al programa)#
def dist_exponencial(n):
    numeros_dist_exponencial=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_exponencial[x]=numero_dist_exponencial(lambde)
    return(numeros_dist_exponencial)

#Generacion de n numeros gamma (ingreso en llamada al programa)#
def dist_gamma(n):
    numeros_dist_gamma=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_gamma[x]=numero_dist_gamma(alfa,beta)
    return(numeros_dist_gamma)

#Generacion de n numeros normales (ingreso en llamada al programa)#
def dist_normal(n):
    numeros_dist_normal=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_normal[x]=numero_dist_normal(mu,sigma)
    return(numeros_dist_normal)

#Generacion de n numeros pascales (ingreso en llamada al programa)#
def dist_pascal(n):
    numeros_dist_pascal=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_pascal[x]=numero_dist_pascal(n1,p)
    return(numeros_dist_pascal)

#Generacion de n numeros binomiales (ingreso en llamada al programa)#
def dist_binomial(n):
    numeros_dist_binomial=[0 for x in range(n)]     
    for x in range(n):
        numeros_dist_binomial[x]=numero_dist_binomial(n1,p)
    return(numeros_dist_binomial)

#Generacion de n numeros hipergeometricos (ingreso en llamada al programa)#
def dist_hipergeometrica(n):
    numeros_dist_hipergeometrica=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_hipergeometrica[x]=numero_dist_hipergeometrica(N,n2,N)
    return(numeros_dist_hipergeometrica)

#Generacion de n numeros poisson (ingreso en llamada al programa)#
def dist_poisson(n):
    numeros_dist_poisson=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_poisson[x]=numero_dist_poisson(N,n2,N)
    return(numeros_dist_poisson)

#Generacion de n numeros poisson (ingreso en llamada al programa)#
def dist_ed(n):
    numeros_dist_ed=[0 for x in range(n)]
    for x in range(n):
        numeros_dist_ed[x]=numero_dist_ed(val,prob)
    return(numeros_dist_ed)









#Generacion de grafica de frecuencia#
def grafica_frecuencias(numeros_dist,dist):
    plt.figure()
    plt.hist(numeros_dist, bins=10, edgecolor="black")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.title("Distribucion "+dist)
    plt.savefig("dist_"+dist+".jpg")








#Llamadas#
numeros=[0 for x in range(n)]
numeros=dist_exponencial(n)
grafica_frecuencias(numeros,"exponencial")

