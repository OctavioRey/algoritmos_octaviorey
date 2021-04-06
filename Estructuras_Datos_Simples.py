#! ESTRUCTURAS DE DATOS SIMPLES VECTORES Y MATRICES

""" vector = [[1] * 3, [2] * 3 , [3] * 3]

for i in range(0, len(vector)):
    print (vector[i]) """


# hola -> aloh


# SLICING (Cortar Vector)


def invertir_cadena(cadena):
    if(len(cadena) == 0):
      return  ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])      #:-1 logra que vaya cortando la cadena a partir desde la ultima posición/letra

print (invertir_cadena("hola"))


