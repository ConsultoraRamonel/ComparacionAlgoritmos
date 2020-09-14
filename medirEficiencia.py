from algoritmos import algoritmo1, algoritmo2
from algoritmos import cargarDatos
import time
print("cargando datos")
datos = cargarDatos("datos.csv")
print("iniciando la pruebas")
# archivo para guardar datos del primer algoritmo
f1 = open("tiempoAlgoritmo1.csv", "w")
# archivo para guardar datos del segundo algoritmo
f2 = open("tiempoAlgoritmo2.csv", "w")


def cronometrarAlgoritmo(algoritmo, archivo):
    # probrar el algoritmo para todos los datos y encontrar el tiempo que demora en ejecutarse
    for i in datos[0]:
        incio = time.time()  # inicia un cronometro
        algoritmo(i, datos)
        fin = time.time()  # detiene el cronometro
        archivo.write(str(fin - incio) + "\n")


cronometrarAlgoritmo(algoritmo1, f1)

cronometrarAlgoritmo(algoritmo2, f2)
