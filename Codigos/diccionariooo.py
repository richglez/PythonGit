libro = {}
estudiante = {}
estudiante["rut"] = "11-1"
estudiante["nombre"] = "nombre1"
estudiante["edad"] = "11"

libro["11-1"] = estudiante




estudiante = {}
estudiante["rut"] = "22-2"
estudiante["nombre"] = "nombre2"
estudiante["edad"] = "22"

libro["22-2"] = estudiante







estudiante = {}
estudiante["rut"] = "44-4"
estudiante["nombre"] = "nombre4"
estudiante["edad"] = "44"

libro["44-4"] = estudiante


for rut in libro:
    estudiante = libro[rut]
    print(estudiante["rut"],"-",estudiante["nombre"],"-",estudiante["edad"])