import serial  # подключаем библиотеку для последовательной связи
import time  # подключаем библиотеку чтобы задействовать функции задержки в программе

ArduinoSerial = serial.Serial('com10', 9600)  # создаем объект для работы с портом последовательной связи
time.sleep(2)  # ждем 2 секунды чтобы установилась последовательная связь
print(ArduinoSerial.readline())  # считываем данные из последовательного порта и печатаем их в виде строки
print("Enter 1 to turn ON LED and 0 to turn OFF LED")

while 1:
    ArduinoSerial.write(b'10000000')   #передаем 1
    time.sleep(1)

