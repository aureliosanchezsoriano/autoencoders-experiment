import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

# GPIO
SENSOR_PIN = 17  # GPIO17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Logs are accessible through apache server
DIRECTORIO_LOGS = "/var/www/html/logs" 

if not os.path.exists(DIRECTORIO_LOGS):
    os.makedirs(DIRECTORIO_LOGS)

# Writing in csv file
def registrar_movimiento(fecha_hora):
    # YYYY-MM-DD.csv
    nombre_archivo = os.path.join(DIRECTORIO_LOGS, f"{fecha_hora.split()[0]}.csv")
    
    with open(nombre_archivo, "a") as archivo:
        archivo.write(f"{fecha_hora}\n")

try:
    fecha_actual = datetime.now().strftime("%Y-%m-%d") # Current date
    while True:
        if GPIO.input(SENSOR_PIN):  # Movement detected
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            registrar_movimiento(fecha_hora)
            time.sleep(1)  # delay
            
        # Update date and time if day changes
        nueva_fecha = datetime.now().strftime("%Y-%m-%d")
        if nueva_fecha != fecha_actual:
            fecha_actual = nueva_fecha

        time.sleep(0.1)  # delay
except KeyboardInterrupt:
    print("Leaving...")
finally:
    GPIO.cleanup()

