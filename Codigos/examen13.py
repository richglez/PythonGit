d1={"L A":5890, "F R":9875,"Rocio N":8745,"Sara M":6987}

for clave in d1.keys():
    if d1[clave]>8000:
        print(clave,end=",")