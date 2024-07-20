from datetime import datetime
import os

path = os.path.dirname(__file__)
actual = datetime.now().strftime("Fecha actual: %Y-%m-%d %H:%M:%S")

with open(os.path.join(path, 'fecha_texto.txt'),'w') as file:
    file.write(actual) 