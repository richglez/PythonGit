#LABORATORIO 3
#Seguramente has visto un display de siete segmentos.

#Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. 
# Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia artículo.

#Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

#Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

digitos = {'0':('###','# #','# #','# #','###'),
           '1':('  #','  #','  #','  #','  #'),
           '2':('###','  #','###','#  ','###'),
           '3':('###','  #','###','  #','###'),
           '4':('# #','# #','###','  #','  #'),
           '5':('###','#  ','###','  #','###'),
           '6':('###','#  ','###','# #','###'),
           '7':('###','  #','  #','  #','  #'),
           '8':('###','# #','###','# #','###'),
           '9':('###','# #','###','  #','  #')}

def Digitos(num):
  for fila in range(len(digitos['0'])):  # digitos  =  3 filas   #5columnas
    print(' '.join(digitos[i][fila] for i in num))  #imprimira los numeros en una sola cadena

num = str(int(input("Ingresa el número que deseas mostrar: ")))
Digitos(num)
