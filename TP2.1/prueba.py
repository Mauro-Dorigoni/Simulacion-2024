import sys
import matplotlib.pyplot as plt
from PIL import Image


print('Parámetros: Los valores deben de cumplir: Xo ≥ 0 || A ≥ 0 || C ≥ 0 || M ≥ Xo, A')

try:
    semilla = int(input('Ingrese el valor de Xo: '))
    a = 1664525
    c = 1013904223
    m = 2**32  # 4294967296

    if semilla >= 0 and a >= 0 and c >= 0 and m > semilla and m > a:
        corridas = int(input('Ingrese las corridas a generar: '))

        resultados = []

        for x in range(corridas):
            subtotal = semilla * a + c
            pseudoaleatorio = subtotal % m
            random = pseudoaleatorio / (m - 1)
            print(f'Random: {random}')
            resultados.append((x, pseudoaleatorio))
            semilla = pseudoaleatorio

            if pseudoaleatorio == 0:
                print('Límite del Método.')
                break

        # Crear la gráfica
        i=0
        y=0
        img = Image.new( 'RGB', (100,100), "black")
        pixels = img.load()
        for x in range(10000):
            aux=str(resultados[x][1])
            prueba=int(aux[0])
            if(prueba % 2 == 0):
                pixels[i,y] = (255,255,255)
            if(y+1>=100):
                y=0
                i=i+1
            else: y=y+1
        img.show()

        print('Programa finalizado.')
    else:
        print('Debe proporcionar valores mayores a cero, o que cumplan con los parámetros.')

except ValueError:
    # sys.exc_info() Muestra el tipo de error
    print('Tienes un error de tipo: ', sys.exc_info()[0])
    print('Nota: Debes introducir valores de tipo numérico.')