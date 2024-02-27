# 1: Dada  la  estabilidad  económica  que  existe  en  un  determinado  país  de  América Latina,  las agencias  automotrices  comienzan  a  ofrecer  distintos  planes  de  financiamiento  para  la comercialización de sus vehículos.  La empresa XGW ofrece el siguiente plan de financiación: dado el monto total del vehículo, el cliente debe pagar el 35% de enganche y el resto en 18 mensualidades iguales sin intereses.  Construya el programa que permita obtener cual es el importe del enganche y la mensualidad quedebe pagar. De igual forma ofrece un plan de hasta  36  meses  con  un  enganche  del  35%,  pero  aplicando  una  tasa  de  interés  global  del 12%.Dentro de tu programa despliega las dos opciones de crédito.

monto = float(input("Introduzca el monto total de su vehiculo:$ "))
credito = int(input("Elige la opcion de pago que mas te convenga(1 o 2): "))

if credito==1:
    importe = monto*0.35
    pago_por_mes = monto/18
    print ("El importe es:$ "),importe
    print ("El pago por mes es:$ "),pago_por_mes

if credito==2:
    importe = monto*0.35
    pago_por_mes = monto/12

    print ("El importe es:$ "),importe
    print ("El pago por mes es:$ "),pago_por_mes

