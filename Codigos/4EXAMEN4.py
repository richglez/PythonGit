#encriptar y desencriptar numeros

def encripta(num):
    n=[]
    while num!=0:
        n.append(((num%10)+7)%10)
        num//=10
        n.reverse()
    num = n[0]*10 + n[1]*1 + n[2]*1000 + n[3]*100
    return num

def desencripta(num):
    n=[]
    while num!=0:
        n.append(((num%10)+3)%10)
        num//=10
    n.reverse()
    num=n[0]*10 + n[1]*1 + n[2]*1000 + n[3]*100
    return num


resp='s'
while resp=='s':
    numero = int(input("Ingresa tu numero:"))
    x=encripta(numero)
    print("Numero encriptado",x)
    y=desencripta(x)
    print("Numero desencriptado",y)
    resp=input("Repetir proceso s/n: ")

