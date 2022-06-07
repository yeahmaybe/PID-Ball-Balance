import serial  # подключаем библиотеку для последовательной связи
import time  # подключаем библиотеку чтобы задействовать функции задержки в программе
from parameters import *

arduino = serial.Serial(port=com_port, baudrate=com_speed, timeout=0)
time.sleep(1)  # ждем 1 секунду чтобы установилась последовательная связь


def transfer_coordinates(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    arduino.write(str(chr(int(x))).encode())
    arduino.write(str(chr(int(y))).encode())