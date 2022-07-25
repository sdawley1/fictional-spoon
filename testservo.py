import serial
import time

serial = serial.Serial('COM5', 9600)
serial.timeout = 0.5

while True:
    i = input("enter angle: ").strip()

    serial.write(i.encode())
    time.sleep(0.5)
    print('moved to: ', serial.readline().decode('ascii'))

serialcomm.close()

