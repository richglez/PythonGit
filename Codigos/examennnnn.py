def operacion (num1,num2,op):
    if op=="suma":
        return num1 + num2
    elif op=="resta":
        return num1-num2
    elif op=="division":
        return num1//num2
    elif op=="multiplicacion":
        return num1*num2
    else:
        return
print(operacion(10,2,"division"))