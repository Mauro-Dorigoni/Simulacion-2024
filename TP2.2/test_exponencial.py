import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from scipy.stats import kstest

# Paso 1: Definir parámetros
lam = 0.5  # Tasa de llegada (lambda) para la distribución exponencial

# Paso 2: Generar muestras
n_samples = 1000
expon_samples = np.random.exponential(scale=1/lam, size=n_samples)

# Paso 3: Verificar la forma de la distribución
plt.hist(expon_samples, bins=30, density=True, alpha=0.6, color='g')
x = np.linspace(0, np.max(expon_samples), 100)
plt.plot(x, expon.pdf(x, scale=1/lam), 'r--', linewidth=2)
plt.xlabel('Valores Generados')
plt.ylabel('Densidad de Probabilidad')
plt.title('Histograma y PDF de la Distribución Exponencial')
plt.legend(['PDF', 'Histograma'])
plt.grid(True)
plt.show()

# Paso 4: Pruebas estadísticas
ks_statistic, p_value_ks = kstest(expon_samples, 'expon', args=(0, 1/lam))

print(f"Prueba de Kolmogorov-Smirnov: Estadístico = {ks_statistic}, p-valor = {p_value_ks}")