import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from scipy.stats import chi2
from scipy.stats import kstest
# Generación de muestras con un tamaño menor
n_samples = 100
uniform_samples = np.random.uniform(0, 1, n_samples)

# Realizar prueba de Kolmogorov-Smirnov
ks_statistic, p_value_ks = kstest(uniform_samples, 'uniform', args=(0, 1))

print(f"Prueba de Kolmogorov-Smirnov (n = {n_samples}): Estadístico = {ks_statistic}, p-valor = {p_value_ks}")