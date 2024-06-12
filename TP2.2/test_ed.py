import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Paso 1: Definir la distribución empírica discreta
valores = np.array([1, 2, 3, 4, 5])
probabilidades = np.array([0.1, 0.2, 0.3, 0.2, 0.2])

# Paso 2: Generar muestras
n_samples = 1000
empirical_samples = np.random.choice(valores, size=n_samples, p=probabilidades)

# Paso 3: Verificar la forma de la distribución
plt.hist(empirical_samples, bins=np.arange(np.min(valores), np.max(valores)+2)-0.5, density=True, alpha=0.6, color='g')
plt.xticks(valores)
plt.xlabel('Valores Generados')
plt.ylabel('Probabilidad')
plt.title('Histograma de la Distribución Empírica Discreta')
plt.grid(True)
plt.show()

# Paso 4: Pruebas estadísticas
expected_counts = n_samples * probabilidades
chi_statistic, p_value_chi = chisquare(np.histogram(empirical_samples, bins=np.arange(np.min(valores), np.max(valores)+2)-0.5)[0], f_exp=expected_counts)

print(f"Prueba de Chi-cuadrado: Estadístico = {chi_statistic}, p-valor = {p_value_chi}")
