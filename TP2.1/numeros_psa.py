import random
from PIL import Image
import array as arr
import statistics
import math
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

semilla=97314

def vonNewman (semilla):
    s_str=str(semilla*semilla)
    while len(s_str)!=10:
        s_str="0"+s_str
    n_rand=(int(s_str[2:7]))
    return n_rand

img = Image.new( 'RGB', (100,100), "black")
pixels = img.load()
for x in range(100):
    for y in range(100):
        semilla=vonNewman(semilla)
        aux=str(semilla)
        prueba=int(aux[0])
        if(semilla):
            print(semilla)
        if(prueba % 2 == 0):
            pixels[x,y] = (255,255,255)
img.show()
