

#! 5! = 5 * 4 * 3 * 2 * 1 = 120
#! 5! = 5 * 4!
#! 4! = 4 * 3!

""" def factorial_i(numero):
    factorial = 1
    for i in range(2,6):
        factorial = factorial * i
    
    return factorial 


def factorial_R(numero):
    if(numero == 1 or numero == 0):
        return 1
    else:
        return numero * factorial_R(numero-1) """

""" print (factorial_R(5))
print(factorial_i(5))  """

def fibonacci_I(numero):
    fib_1 = 0
    fib_2 = 1
    fibonacci = 0
    for i in range (2, numero + 1):               #Iterativo
        fibonacci = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fibonacci
    return fibonacci

#1 fib(n) = fib(n-1) + fib(n-2)

def fibonacci_R(numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return fibonacci_R(numero - 1) + fibonacci_R(numero - 2)      #Recursivo

print(fibonacci_R(8))

print (fibonacci_I(8))
