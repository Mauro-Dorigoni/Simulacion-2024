import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import kstest

# Paso 1: Definir parámetros
lam = 3  # Parámetro lambda de la distribución de Poisson

# Paso 2: Generar muestras
n_samples = 1000
poisson_samples = np.random.poisson(lam, n_samples)

# Paso 3: Verificar la forma de la distribución
plt.hist(poisson_samples, bins=np.arange(np.min(poisson_samples), np.max(poisson_samples)+2)-0.5, density=True, alpha=0.6, color='g')
x = np.arange(np.min(poisson_samples), np.max(poisson_samples) + 1)
plt.plot(x, poisson.pmf(x, lam), 'ro-', markersize=5)
plt.xlabel('Valores Generados')
plt.ylabel('Probabilidad')
plt.title('Histograma y PMF de la Distribución de Poisson')
plt.legend(['PMF', 'Histograma'])
plt.grid(True)
plt.show()

# Paso 4: Pruebas estadísticas
ks_statistic, p_value_ks = kstest(poisson_samples, 'poisson', args=(lam,))

print(f"Prueba de Kolmogorov-Smirnov: Estadístico = {ks_statistic}, p-valor = {p_value_ks}")

