import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import kstest

# Paso 1: Definir parámetros
mu = 0  # Media de la distribución normal
sigma = 1  # Desviación estándar de la distribución normal

# Paso 2: Generar muestras
n_samples = 1000
normal_samples = np.random.normal(mu, sigma, n_samples)

# Paso 3: Verificar la forma de la distribución
plt.hist(normal_samples, bins=30, density=True, alpha=0.6, color='g')
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
plt.plot(x, norm.pdf(x, mu, sigma), 'r--', linewidth=2)
plt.xlabel('Valores Generados')
plt.ylabel('Densidad de Probabilidad')
plt.title('Histograma y PDF de la Distribución Normal')
plt.legend(['PDF', 'Histograma'])
plt.grid(True)
plt.show()

# Paso 4: Pruebas estadísticas
ks_statistic, p_value_ks = kstest(normal_samples, 'norm', args=(mu, sigma))

print(f"Prueba de Kolmogorov-Smirnov: Estadístico = {ks_statistic}, p-valor = {p_value_ks}")
