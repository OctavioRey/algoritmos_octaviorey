# Ejercicio 2

""" def suma_R(numero):
    if (numero == 0 or numero == 1):
        return numero
    else:
        return numero + suma_R(numero-1)

print (suma_R(4)) """

# Ejercicio 3

""" def producto_R(numero1, numero2):
    if (numero1 == 0 or numero2 == 0):
        return 0
    else:
        return (numero1 + producto_R(numero1, numero2-1)) 

print (producto_R(3,0)) """

#Ejercicio 7

""" def sumatoria_R(numero):
    if (numero == 1):
        return numero
    else:
        return 1/numero + sumatoria_R(numero-1)

print (sumatoria_R(3))
 """

#Ejercicio Logaritmo

def logaritmo(numero, base):
    if(numero / base < 1):
        return 0
    else:
        return 1 + logaritmo(numero/base , base)

print (logaritmo(8, 2))