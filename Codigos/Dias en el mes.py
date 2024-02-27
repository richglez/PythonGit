#Cada año divisible por 4 es bisiesto, con la excepción de los años que finalizan en 00, esto es, divisible por 100, y no divisible por 400.  Elabora un programa que solicite el mes (1 al 12, en donde 1 es enero, 2 febrero, etc) y determine el número de días del mes, si el mes es dos deberá solicitar el año y determinar si tiene 28 o29 días.

mes = int(input("Ingrece el mes en numero (1 es enero, 2 febrero, etc): "))
año = int(input("Ingrece el año: "))


if mes<=0 and año<=0:
    print("ERROR")
#Todos los años que terminan en 00, por ejemplo 2000 van a ser bisiesto
if año % 4 ==0 and año % 100 != 0 or año % 400 ==0:
    print("Es bisiesto")
if mes in (1, 3, 5, 7, 8, 10, 12):
    print("31 dias")


if mes == 2:
    print("28/29 dias")


if mes in (4, 6, 9, 11):
    print("30 dias")





    
