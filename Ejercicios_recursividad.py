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

''' def logaritmo(numero, base):
    if(numero / base < 1):
        return 0
    else:
        return 1 + logaritmo(numero/base , base)

print (logaritmo(8, 2)) '''


#Ordenamiento Quicksort

datos = [11, 3, 81, 7, 45, 20, 4, 5, 10, 22, 30, 25]

def quicksort(vector, inicio, fin):
    
    primero = inicio
    ultimo = fin-1
    pivote = fin
    while(primero < ultimo):
        while(vector[primero] <= vector[pivote] and primero <= ultimo):
            primero += 1
        while(vector[ultimo]> vector[pivote] and ultimo >= primero):
            ultimo -= 1

        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if (vector[pivote] < vector[primero]):
        vector[pivote], vector[primero] = vector[primero], vector[pivote]

    if(inicio < ultimo):
        quicksort(vector, inicio, primero -1)
    if(primero < fin):
        quicksort(vector, primero + 1, fin)


# Busqueda Binaria Recursiva

def busqueda_binaria_R(vector, buscado, inicio, fin):
    
    if(inicio <= fin):
        medio = (inicio + fin ) // 2
        if(vector[medio] == buscado ):
            return medio
        elif(vector[medio] < buscado):     
            return busqueda_binaria_R(vector, buscado, medio+1, fin)
        else:
            return busqueda_binaria_R(vector, buscado, inicio, medio-1)
    else:
        return -1

quicksort(datos, 0, (len(datos)-1))
print (datos)
print (busqueda_binaria_R(datos, 81, 0, len(datos)-1))

