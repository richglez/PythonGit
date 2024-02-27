def SeriesNumeros():
    print()
    n_inicial=int(input("Ingrese el numero inicial de la serie: "))
    n_final=int(input("Ingrese el numero final de la serie: "))
    incremento=int(input("Ingrese el numero de incremento de la serie: "))
    for i in range(n_inicial,n_final+1,incremento):
        print(i)