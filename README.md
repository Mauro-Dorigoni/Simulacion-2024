# Simulacion-2024
## Trabajo Practico Simulacion Ruleta casino
### Calculo de estadisticos
    Sea xi un numero arrojado por una tirada de la ruleta (xi entero entre 0 y 36)
    Sea n la cantidad de veces que se tira la ruleta
    Sea fri la frecuencia relatica de aparicion de cada xi (calculado como la frecuancia absoluta de aparicion sobre n)
    Entonces
        promedio = x(raya) = (Σxi)/n
        fri = fai/n
        Varianza = var = Σ (((xi - promedio)^2))*fri
        Desvio = σ = var^(0.5)
    Para los valores esperados, se toma que la fr de cada numero posible es 1/37, por lo tanto
        promedio_esperado= (0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35+36)/37 = 18
        fri_esperada = 1/37
        var_esperada = Σ (((x - 18)^2))*1/37 con x enteros entre 0 y 36
        desv_esperado = var_esperada^(0.5)