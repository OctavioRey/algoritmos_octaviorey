
# Ejercicio 2

""" def suma_R(numero):
    if (numero == 0 or numero == 1):
        return numero
    else:
        return numero + suma_R(numero-1)

print (suma_R(4)) """

# Ejercicio 3

def producto_R(numero1, numero2):
    if (numero1 == 0 or numero2 == 0):
        return 0
    else:
        return (numero1 + producto_R(numero1, numero2-1)) 

print (producto_R(3,5))

#Ejercicio 4