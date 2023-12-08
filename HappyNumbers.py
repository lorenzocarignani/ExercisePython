'''Ejercicio 1 – Happy Numbers 
Hacer un programa que imprima los X primeros “happy numbers”. Ver definición en https://en.wikipedia.org/wiki/Happy_number. 
Variantes (opcionales) 
a) Modificar el programa para que tanto el valor final al que hay que llegar (1 en el caso de los happy numbers) como la potencia aplicada (2 en el caso de los happy numbers) sean parametrizables. 
b) Aplicar alguna optimización, suponiendo que la memoria no es problema'''

# Lorenzo Carignani


def sum_square_numbers(n ,power = 2):
    sum = 0 
    while n > 0: 
        digit = n % 10 
        sum += pow(digit ,power) 
        n //= 10 
    return sum

#Comprueba que es un numero feliz
def is_happy_number(n, final_value = 1 , power = 2):
    slow = n
    fast = n
    while True:
        slow = sum_square_numbers(slow, power)
        fast = sum_square_numbers(sum_square_numbers(fast, power), power)
        if slow == final_value or fast == final_value:
            return True
        if slow == fast:
            return False

 
def search_happy_numbers(X, final_value= 1, power = 2 ):
    happy_number = [] 
    n = 1 
    while len(happy_number) < X: 
        if is_happy_number(n , final_value , power): 
            happy_number.append(n)  
        n += 1          
    return happy_number 


def validate_input(message, min_value):
    while True:
        try:
            value = int(input(message))
            if value <= min_value:
                print(f"Ingrese un valor mayor a {min_value}")
            else:
                return value
        except ValueError:
            print("Ingrese un número válido.")

X = validate_input("Ingrese la cantidad de números felices que quiere buscar: ", 0)
final_value = validate_input("Ingrese el valor final a buscar: ", 0)
power = validate_input("Ingrese la potencia: ", 0)


search_numbers = search_happy_numbers(X, final_value, power)

print(f"Los {X} primeros números felices son: {search_numbers}")
