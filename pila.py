
class Pila(object):
    
    def __init__(self):
        self.__elementos = []           # Los dos guiones bajos hacen al atributo privado, y no se le puede acceder a éste desde afuera de la class

    def push(self, dato):
        self.__elementos.append(dato)





pila = Pila()


pila.push(5)
pila.push(3)
pila.push(2)
pila.push(8)


print (pila.elementos)




