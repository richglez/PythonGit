voto=1  #un voto por persona
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0


print ("SISTEMA DE ELECCIONES")
print()
#mientras el voto sea diferente de cero vas a hacer esto:
while voto!=0:
    voto=int(input("Seleccione el numero de candidato a votar, para salir digite 0: "))
    if voto==1:
        cand1+=1
    elif voto==2:
        cand2+=1
    elif voto==3:
        cand3+=1
    elif voto==4:
        cand4+=1
    else:
        print("Saliste de las votaciones, gracias")

print()
print()
#resultados
print("Los resultados fueron:")
print()
suma_votos=cand1+cand2+cand3+cand4    #para sacar el porcentaje
print("Candidato 1 tuvo:",cand1,"Votos. -- Procentaje:",format(cand1/suma_votos*100,".2f"))
print("Candidato 2 tuvo:",cand2,"Votos. -- Procentaje:",format(cand2/suma_votos*100,".2f"))
print("Candidato 3 tuvo:",cand3,"Votos. -- Procentaje:",format(cand3/suma_votos*100,".2f"))
print("Candidato 4 tuvo:",cand4,"Votos. -- Procentaje:",format(cand4/suma_votos*100,".2f"))

#QUIEN GANO????
print(0)
if cand1>cand2 and cand1>cand3 and cand1>cand4:
    print("Gana el candidato 1!")
elif cand2>cand3 and cand2>cand4:
    print("Gana el candidato 2!")
elif cand3>cand4:
    print("Gana el candidato 3!")
else:
    print("Gana el candidato 4!")


