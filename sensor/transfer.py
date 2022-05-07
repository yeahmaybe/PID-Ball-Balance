import serial  # подключаем библиотеку для последовательной связи
import time  # подключаем библиотеку чтобы задействовать функции задержки в программе
from parameters import *

ArduinoSerial = serial.Serial(com_port, com_speed)  # создаем объект для работы с портом последовательной связи
time.sleep(2)  # ждем 2 секунды чтобы установилась последовательная связь


def transfer_coordinates(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    print(bin(x), bin(y))

    bin_x = bin(x).replace("0b", "")
    bin_y = bin(y).replace("0b", "")

    while len(bin_x) < byte_length:
        bin_x = '0' + bin_x

    while len(bin_y) < byte_length:
        bin_y = '0' + bin_y

    print(bin_x, bin_y)
    bin_coordinates = bin_x + bin_y
    bin_coordinates = bytes(bin_coordinates, 'ascii')
    print(bin_coordinates)
    ArduinoSerial.write(bin_coordinates)
    time.sleep(1)
