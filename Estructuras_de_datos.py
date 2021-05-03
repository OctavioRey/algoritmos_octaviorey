#! int, float, string

datos = [1 , 2 ,3]


def prueba(num1, num2, cad, vector):
    num1= num2 * 2
    cad = "mundo"
    vector[0] = 100

num1 = 2
num2 = 5
cadena = "hola"

prueba (num1, num2, cadena, datos)

print (num1, num2, cadena)
print (datos)

num1 = 1
num2 = num1
num2 = num2 + 3

print (num1, num2)

''' lista1 = [1, 2, 3, 4]
lista2 = lista1
lista2[1] = 7
lista3 = lista2

lista3.append(87)

print(lista1, lista2, lista3) '''

''' lista1 = {'a': True}
lista2 = {'a': True}

print (lista1 == lista2)
 '''

class Persona(object):

    edad = None


num1 = Persona()
num1.edad = 10 

num2 = Persona()
num2.edad = 10

print (num1 == num2)          # Esto compara el "registro" en su totalidad y no sólo el campo de edad, por ende es falso.
print (num1.edad == num2.edad) # Esto sí compara el campo de edad, por ende el outcome es verdadero.