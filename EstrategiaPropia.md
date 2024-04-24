Apuesta mininma 3500
# Estrategia Propia
## Funcionamiento de la estrategia de la proporción constante
La estrategia de la proporción constante es muy parecida a la de la apuesta constante, pero con un elemento adicional. Cuando se utiliza la estrategia de la apuesta constante, el importe apostado es el mismo tanto si el jugador gana como si pierde. Sin embargo, la estrategia de la proporción constante utiliza importes de apuesta variables que cambian según los resultados previos.

Por lo tanto, si un jugador tiene una buena racha y está ganando, el importe de la apuesta aumentará para que pueda ganar aún más. Pero si está perdiendo dinero, el importe de la apuesta se reducirá lentamente y sus pérdidas potenciales no aumentarán tan rápido como si utilizara la estrategia de la apuesta constante. Este mecanismo autorregulador es lo que hace que la estrategia de la proporción constante sea un poco más avanzada que la estrategia de la apuesta constante.

 EJEMPLO
Para que todo quede muy claro, vamos a ver un ejemplo de la estrategia de la proporción constante en acción. Imaginemos que el jugador quiere apostar un 10% de su presupuesto en una apuesta de color. Empieza con 100 $ y hace una apuesta de 10 $ al rojo. Si gana, tendrá 110 $ y en la siguiente ronda apostará 11 $. Si pierde, se quedará con 90 $ y en la siguiente ronda solo apostará 9 $. El jugador debe seguir este patrón de apuestas hasta que se quede sin dinero o decida dejar de jugar.

Al igual de lo que sucede con la estrategia de la apuesta constante, en la estrategia de la proporción constante también hay que encontrar un equilibrio entre:

Una volatilidad alta: posibilidad de conseguir grandes premios, pero también de perderlo todo rápidamente.
Una volatilidad baja: las posibles ganancias son más pequeñas, pero también hay menos probabilidades (o casi ninguna) de perder todo el dinero rápidamente.
La volatilidad alta se consigue con tipos de apuesta más volátiles y con importes más elevados. La volatilidad baja se consigue con tipos de apuesta menos volátiles y con importes más bajos. Si apuestas todo tu presupuesto a un número directo, lo más probable es que lo pierdas todo en una sola ronda; en cambio, si apuestas un 1% de tu presupuesto al rojo o al negro, tu presupuesto inicial fluctuará ligeramente, aunque tus probabilidades de acabar con menos dinero del que tenías al empezar a jugar son mayores.

Obviamente, el mejor escenario está a medio camino entre ambos extremos, y utilizaré mis simulaciones para determinar el motivo.

## Redondeo de la apuesta y límites de apuesta mínimos
Hay que tener en cuenta dos posibles problemas. Al apostar una proporción fija del presupuesto, la cantidad que debes poner en juego no será siempre "bonita" o redonda. Si no puedes apostar la cantidad exacta que exigen tus cálculos, redondéala hacia arriba o hacia abajo, según te convenga .

Si no tienes suerte y el importe que debes apostar es inferior a la apuesta mínima de la mesa de ruleta, juega este importe y sigue adelante. Es el enfoque que he usado en mis simulaciones.

## Simulaciones de la estrategia de la proporción constante
Las simulaciones rigurosas son la mejor forma de ver cómo funciona esta estrategia y de comprobar que los pequeños cambios en el estilo de juego pueden tener un gran impacto en los resultados esperados. He utilizado varias simulaciones para probar distintos tipos de apuesta con la estrategia de la proporción constante y averiguar el porcentaje óptimo del presupuesto que deberías apostar en cada caso.

## Metodología y variables utilizadas
Todas las simulaciones se han realizado usando mi software de simulación, que incluye reglas, probabilidades y pagos para la ruleta de un cero sin reglas especiales (como En prison o Le partage). Si juegas con la ruleta europea clásica, los resultados deberían parecerse mucho a los de mis simulaciones.

Los jugadores empezaban con un presupuesto de 100 $ y procedían de la siguiente manera:

Hacían el mismo tipo de apuesta (color, esquina o directa) una y otra vez, pero con un importe de apuesta variable.
El importe de apuesta se calculó como una proporción fija del presupuesto de cada momento, redondeado a la unidad más cercana.
El importe mínimo de la apuesta se fijó en 1 $. Si el importe de apuesta calculado era inferior a 1 $, se jugaba el importe mínimo.
Los jugadores seguían apostando hasta perder todo su presupuesto o hasta completar 100 giros.
En cuanto a los tipos de apuesta utilizados, tuve en cuenta todas las alternativas y decidí utilizar las siguientes:

Color: rojo o negro (probabilidad de ganar: 18/37; pago: x2)
Esquina: cuatro números que comparten una esquina (probabilidad de ganar: 4/37; pago: x9)
Directa: un número (probabilidad de ganar: 1/37; pago: x36)

## Modificacion para presupuesto infinito
El jugador empieza con una apuesta de 3500. Siempre y cuando el jugador genere ganancias, apuesta el xx% de estas. Si el jugador presenta perdidas, apostara el xx% del valor absoluto de sus perdidas.