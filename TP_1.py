# Ejercicio 8

# def decimal_a_binario(numero):

#     if numero == 0:
#         return ""
#     else:
#         return decimal_a_binario(numero // 2) + str(numero % 2)

# print (decimal_a_binario(28))

# Ejercicio 5


# Valores = {"": 0, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

# def romano_a_decimal(romano):

#     if romano in Valores:
#          return Valores[romano]

#     primero, segundo = map(romano_a_decimal, romano[:2])
#     if primero < segundo:
#         return segundo - primero + romano_a_decimal(romano[2:])
#     else:
#         return primero + romano_a_decimal(romano[1:])

# print (romano_a_decimal('IV'))

# Ejercicio 22

# datos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mochila = ['Pan', 'Capa', 'Sable de luz', 'otro']

# def usar_fuerza(mochila, pos):
#     if(pos< len(mochila)):
#         if(mochila[pos] == 'Sable de luz'):
#             return  print('El Sable de luz se encuentra en la mochila, la cantidad de objetos que se sacó fue: ' ,pos)
#         else:
#             return usar_fuerza(mochila, pos+1)
#     else:
#         return -1

# print(usar_fuerza(mochila, 0))


# Ejercicio 23

# def salida_laberinto(matriz, x, y, caminos=[]):
#     """Salida del laberinto."""
#     if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
#         if(matriz[x][y] == 2):
#             caminos.append([x, y])
#             print("Saliste del laberinto")
#             print(caminos)
#             caminos.pop()
#         elif(matriz[x][y] == 1):
#             matriz[x][y] = 3
#             caminos.append([x, y])
#             # print("mover este")
#             salida_laberinto(matriz, x, y+1, caminos)
#             # print("mover oeste")
#             salida_laberinto(matriz, x, y-1, caminos)
#             # print("mover norte")
#             salida_laberinto(matriz, x-1, y, caminos)
#             # print("mover sur")
#             salida_laberinto(matriz, x+1, y, caminos)
#             caminos.pop()
#             matriz[x][y] = 1


# lab = [[1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 1, 0, 1],
#        [1, 1, 1, 0, 1, 0, 1],
#        [1, 0, 1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 2]]
    
# salida_laberinto(lab, 0, 0)