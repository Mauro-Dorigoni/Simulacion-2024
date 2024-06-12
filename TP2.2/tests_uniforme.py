import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from scipy.stats import chi2
from scipy.stats import kstest

# Paso 1: Definir un rango
a, b = 0, 1  # Rango para la distribución uniforme

# Paso 2: Generar muestras
n_samples = 1000
uniform_samples = np.random.uniform(a, b, n_samples)

# Paso 3: Verificar la uniformidad
# Prueba de chi-cuadrado
expected_counts = np.ones_like(uniform_samples) * (b - a) / n_samples
chi_statistic = np.sum((np.histogram(uniform_samples, bins=n_samples)[0] - expected_counts) ** 2 / expected_counts)

df = n_samples - 1
p_value_chi = chi2.sf(chi_statistic, df)

print(f"Prueba de Chi-cuadrado: Estadístico = {chi_statistic}, p-valor = {p_value_chi}")

# Prueba de Kolmogorov-Smirnov
ks_statistic, p_value_ks = kstest(uniform_samples, 'uniform', args=(a, b))

print(f"Prueba de Kolmogorov-Smirnov: Estadístico = {ks_statistic}, p-valor = {p_value_ks}")

# Paso 4: Visualización
plt.hist(uniform_samples, bins=20, density=True, alpha=0.6, color='g')
x = np.linspace(a, b, 100)
plt.plot(x, uniform.pdf(x, a, b), 'r--', linewidth=2)
plt.xlabel('Valores Generados')
plt.ylabel('Densidad de Probabilidad')
plt.title('Histograma y PDF de la Distribución Uniforme')
plt.legend(['PDF', 'Histograma'])
plt.grid(True)
plt.show()