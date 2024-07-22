from datetime import datetime
import os

path = os.path.dirname(__file__)
print(f'UBICACION ACTUAL: {path}')
actual = datetime.now().strftime("Fecha: %Y-%m-%d %H:%M:%S")

with open(os.path.join(path, 'fecha_texto.txt'),'w') as file:
    file.write(actual) 
print("ARCHIVO GENERADO  >>>>>>")
