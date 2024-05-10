# Explicacion Estrategias usadas #

## Martingala ##
Idem link mandado por profesor (tanto para banca finita como infinita)

## D´Alambert ##
Idem link mandado por profesor (tanto banca finita como infinita)

## Fibonacci ##
Idem link mandado por profesor (tanto banca finita como infinita)

## Propia - Proporcion constante ##
**Para banca finita:**
- El jugador comienza apostando el 10% de su banca (redondeada al entero mas cercano) al numero ingresado en el llamado al programa
- Tanto como si pierde como si gana, continua apostando el 10% de su banca resultante (redondeada al entero mas cercano) al mismo numero
- Si en algun momento la banca resultante es menor a 10 (diez) unidades monetarias, el jugador apuesta 1 (una) unidad monetaria
**Para banca infinita:**
- El jugador comienza apostando 1 (una) unidad monetaria al numero ingresado en el llamado al programa
- Tanto como si pierde como si gana, continua apostando el 1 (una) unidad monetaria al mismo numero, a menos que logre una banca resultante de valor absoluto mayor a 10. En este caso, comienza a apostar el 10% del valor absoluto de su banca resultante (redondeada al entero mas cercano).


# Aclaraciones pertinentes #
- La apuesta minima se establecio en 1 (una) unidad monetaria
- Las estrategias Martingala, D´Alambert y Fibonacci apuestan al negro
- Los numeros 15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35 y 26 son negros (sacado de ruleta estandar de casino)
- Los colores (en este caso, el negro) pagan 2 a 1
- La estretegia propia (Proporcion constante) apuesta a un numero (ingresado al llamar al programa)
- Un numero paga 36 a 1
- Para las simulaciones con capital finito, se establecio una banca de 100 (cien) unidades monetarias para el jugador
- Las simulaciones con capital finito finalizan cuando ocurre el primero de los siguientes eventos:
    1. El flujo de caja del jugador llega a 0 (cero) unidades monetarias
    2. El flujo de caja del jugador no puede cubrir la totalidad de la siguiente apuesta correspondiente en el algorimo usado
    3. Se han completado todas las tiradas propuestas
- Se propusieron 100 (cien) tiradas, una por ficha inicial que posee el jugador en banca finita
- Se propusieron 5 (cinco) corridas, para evaluar patrones de comportamiento

