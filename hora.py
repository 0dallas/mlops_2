from datetime import datetime
import os


path = os.path.dirname(__file__)
print(f'UBICACION ACTUAL: {path}')
actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(os.path.join(path, 'fecha.txt'),'w') as file:
    file.write(actual) 
print("ARCHIVO GENERADO")
