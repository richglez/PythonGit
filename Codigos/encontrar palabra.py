palabra = input("Ingresa la palabra que deseas encontrar: ").lower()
texto = input("Ingresa el texto escondido: ").lower()

aqui_esta = True

for silaba in palabra:
    buscar = texto.find(silaba)
    if buscar < 0:
        aqui_esta = False
        print("Ingresa texto")
        break
    inicio = buscar + 1
if aqui_esta:
    print("El veredicto final es...\nSI :D")
else:
    print("El veredicto final es...\nNO :(")