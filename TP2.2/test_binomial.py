import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import kstest

# Paso 1: Definir parámetros
n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo

# Paso 2: Generar muestras
n_samples = 1000
binomial_samples = np.random.binomial(n, p, n_samples)

# Paso 3: Verificar la forma de la distribución
plt.hist(binomial_samples, bins=np.arange(0, n+2)-0.5, density=True, alpha=0.6, color='g')
x = np.arange(0, n+1)
plt.plot(x, binom.pmf(x, n, p), 'ro-', markersize=5)
plt.xlabel('Valores Generados')
plt.ylabel('Probabilidad')
plt.title('Histograma y PMF de la Distribución Binomial')
plt.legend(['PMF', 'Histograma'])
plt.grid(True)
plt.show()

# Paso 4: Pruebas estadísticas
ks_statistic, p_value_ks = kstest(binomial_samples, 'binom', args=(n, p))

print(f"Prueba de Kolmogorov-Smirnov: Estadístico = {ks_statistic}, p-valor = {p_value_ks}")