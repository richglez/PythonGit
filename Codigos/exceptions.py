#errores previstos




def sum(x,y):
    c = x+y
    print(c) 

def rest(x,y):
    c = x - y
    print(c) 

def mult(x,y):
    c = x * y
    print(c) 


def div(x,y):
    try:
        c = x / y
        print(c) 
        
    except ZeroDivisionError:  #ZeroDivisionError: division by zero 
        print("ERROR: Zero can't be process as division")




opc = "s"  # Inicializa opc con 's' para que el bucle se ejecute al menos una vez

while opc == 's':
    # Solicitar números al usuario y convertirlos a enteros
    num1 = int(input("\nInsert number 1: "))
    num2 = int(input("Insert number 2: "))
    
    
    operacion = input("Which function would you want: 'sum/rest/mult/div?': ")
    if operacion == "sum":
        sum(num1,num2)
        
    elif operacion == "rest":
        rest(num1,num2)
        
    elif operacion == "mult":
        mult(num1,num2)
        
    elif operacion == "div":
        div(num1,num2)
        
    else:
        print("Funcion no programada :(")

    opc = input("\nDo you want to try again? (s/n):").lower()  # Convertir la entrada a minúsculas para ser insensible a mayúsculas
# El bucle continuará mientras opc sea igual a 's'


