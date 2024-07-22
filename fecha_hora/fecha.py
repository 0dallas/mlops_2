from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('.env.local')
key = os.getenv("CLAVE_PRIVADA")

path = os.path.dirname(__file__)
print(f'UBICACION ACTUAL: {path}')
actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
actual = f"{key} dice: {actual}"

with open(os.path.join(path, 'fecha_texto.txt'),'w') as file:
    file.write(actual) 
print("ARCHIVO GENERADO  >>>>>>")
