import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import scipy.special as sp
from scipy.stats import norm


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






#Metodo de rechazo de distribucion Uniforme#
def densidad_objetivo(x):
    return 2 * x if 0 <= x <= 1 else 0

def metodo_rechazo_uniforme(inferior, superior, M, n):
    resultados = []
    while len(resultados) < n:
        x = numero_dist_uniforme(inferior,superior)
        y = numero_dist_uniforme(inferior,superior)
        if y <= densidad_objetivo(x):
            resultados.append(x)
    return resultados

#Metodo de rechazo de distribucion Exponencial#
def densidad_exponencial(x, lambd):
    return lambd * np.exp(-lambd * x)

def metodo_rechazo_exponencial(lambd, M, n):
    resultados = []
    while len(resultados) < n:
        x = numero_dist_uniforme(0, 10 / lambd)
        y = numero_dist_uniforme(0, M)
        if y <= densidad_exponencial(x, lambd):
            resultados.append(x)
    return resultados

#Metodo de rechazo de distribucion Gamma#
def densidad_gamma(x, alpha, beta):
    if x < 0:
        return 0
    return (beta**alpha * x**(alpha-1) * np.exp(-beta * x)) / sp.gamma(alpha)

def metodo_rechazo_gamma(alpha, beta, n):
    resultados = []
    M = (alpha - 1)**(alpha - 1) * np.exp(1 - alpha)
    while len(resultados) < n:
        x = np.random.uniform(0, 10 * alpha)
        y = np.random.uniform(0, M)
        if y <= densidad_gamma(x, alpha, beta):
            resultados.append(x)
    return resultados


#Metodo de rechazo de distribucion Normal#
def densidad_normal(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma)**2)

def metodo_rechazo_normal(mu, sigma, n):
    resultados = []
    M = 1 / (sigma * np.sqrt(2 * np.pi))
    while len(resultados) < n:
        x = np.random.uniform(mu - 5 * sigma, mu + 5 * sigma)
        y = np.random.uniform(0, M)
        if y <= densidad_normal(x, mu, sigma):
            resultados.append(x)
    return resultados

#Metodo de rechazo de distribucion Pascal#
def pmf_pascal(k, r, p):

    return stats.binom.pmf(k, r, p)

def metodo_rechazo_pascal(r, p, n):
    resultados = []
    M = max(pmf_pascal(k, r, p) for k in range(r, r + 10))
    while len(resultados) < n:
        k = np.random.negative_binomial(r, p)
        y = np.random.uniform(0, M)
        if y <= pmf_pascal(k, r, p):
            resultados.append(k)
    return resultados

#Metodo de rechazo de distribucion Binomial#
def pmf_binomial(k, n, p):
    return stats.binom.pmf(k, n, p)

def metodo_rechazo_binomial(n, p, n_generados):
    resultados = []
    M = max(pmf_binomial(k, n, p) for k in range(n + 1))
    while len(resultados) < n_generados:
        k = np.random.binomial(n, p)
        y = np.random.uniform(0, M)
        if y <= pmf_binomial(k, n, p):
            resultados.append(k)
    return resultados

#Metodo de rechazo de distribucion Hipergeometrica#
def pmf_hipergeometrica(k, N1, N2, n):
    return stats.hypergeom.pmf(k, N1, N2, n)

def metodo_rechazo_hipergeometrica(N1, N2, n, n_generados):
    resultados = []
    M = max(pmf_hipergeometrica(k, N1, N2, n) for k in range(max(0, n - (N1 - N2)), min(N2, n) + 1))
    while len(resultados) < n_generados:
        k = np.random.hypergeometric(N1, N2, n)
        y = np.random.uniform(0, M)
        if y <= pmf_hipergeometrica(k, N1, N2, n):
            resultados.append(k)
    return resultados

#Metodo de rechazo de distribucion Poisson#
def pmf_poisson(k, lmbda):
    return np.exp(-lmbda) * (lmbda ** k) / np.math.factorial(k)

def metodo_rechazo_poisson(lmbda, n):
    resultados = []
    M = max(pmf_poisson(k, lmbda) for k in range(int(lmbda * 3)))
    while len(resultados) < n:
        k = np.random.poisson(lmbda)
        y = np.random.uniform(0, M)
        if y <= pmf_poisson(k, lmbda):
            resultados.append(k)
    return resultados

#Metodo de rechazo de distribucion Empirica Discreta#
def metodo_rechazo_empirica_discreta(valores, probabilidades, n):
    resultados = []
    M = max(probabilidades)
    while len(resultados) < n:
        candidato = np.random.choice(valores, p=probabilidades)
        y = np.random.uniform(0, M)
        if y <= probabilidades[valores.index(candidato)]:
            resultados.append(candidato)
    return resultados


#Funcion inversa de distribucion Uniforme#
def calcular_probabilidad_uniforme(inferior, superior, numeros):
    probabilidad = 1 / (superior - inferior)
    probabilidades = [((x - inferior) / (superior - inferior)) * probabilidad for x in numeros]
    return probabilidades

def inversa_uniforme(inferior, superior, probabilidades):
    inversa=[]
    for x in range(len(probabilidades)):
        inversa[x]=inferior+probabilidades[x]*(superior-inferior)
    return inversa

#Funcion inversa de distribucion Exponencial#
def calcular_probabilidad_acumulada_exponencial(numeros, lambde):
    probabilidades_acumuladas = [1 - np.exp(-lambde * x) for x in numeros]
    return probabilidades_acumuladas

def inversa_exponencial(lambde, probabilidades_acumuladas):
    inversa=[]
    for x in range(len(probabilidades_acumuladas)):
        inversa[x]=-1 / lambde * np.log(1 - probabilidades_acumuladas[x])
    return inversa


#Funcion inversa de distribucion Normal#
def calcular_probabilidad_acumulada_normal(valores, mu, sigma):
    probabilidades_acumuladas = [norm.cdf(x, loc=mu, scale=sigma) for x in valores]
    return probabilidades_acumuladas

def calcular_inversa_normal(probabilidades_acumuladas, mu, sigma):
    inversa=[]
    for x in range(len(probabilidades_acumuladas)):
        inversa[x]=norm.ppf(probabilidades_acumuladas[x], loc=mu, scale=sigma)
    return inversa




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

