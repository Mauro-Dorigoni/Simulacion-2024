import random
import array as arr
import statistics
import math
import sys
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------#
cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls = 0
area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido = 0.0
prob_distrib_demanda = [0.0]*26
tiempo_proximo_evento = [0.0]*5

#-------------------------------------------------------------------------------------------------#
def inicializar():
    global cantidad, bigs, nivel_inv_inicial, nivel_inv, tipo_proximo_evento, num_eventos, num_meses, num_valores_demanda, smalls
    global area_mantenimiento, area_faltante, costo_mantenimiento, costo_incremental, maxlag, media_intervalo_demanda, minlag, costo_setup, costo_faltante, tiempo_simulacion, tiempo_ultimo_evento, costo_total_pedido
    global prob_distrib_demanda
    global tiempo_proximo_evento

    tiempo_simulacion = 0.0
    nivel_inv = nivel_inv_inicial
    tiempo_ultimo_evento = 0.0

    costo_total_pedido = 0.0
    area_mantenimiento = 0.0
    area_faltante = 0.0

    tiempo_proximo_evento[1] = 1.0e+30
    tiempo_proximo_evento[2] = tiempo_simulacion + random.expovariate(media_intervalo_demanda)
    tiempo_proximo_evento[3] = num_meses
    tiempo_proximo_evento[4] = 0.0
    
#-------------------------------------------------------------------------------------------------#
def temporizador():
    print("n")

#-------------------------------------------------------------------------------------------------#
def llegada_pedido():
    print("n")

#-------------------------------------------------------------------------------------------------#
def demanda():
    print("n")

#-------------------------------------------------------------------------------------------------#
def evaluacion():
    print("n")

#-------------------------------------------------------------------------------------------------#
def reporte():
    print("n")

#-------------------------------------------------------------------------------------------------#
def actualizacion_tiempo_prom_estadisticas():
    print("n")

