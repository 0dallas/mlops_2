from datetime import datetime
actual = datetime.now().strftime("Fecha actual: %Y-%m-%d %H:%M:%S")

with open('fecha_texto.txt','w') as file:
    file.write(actual)