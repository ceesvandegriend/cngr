"""
Name:        blink
Author:      Cees van de Griend <cees@griend.eu>
Date:        2022-05-13

Description: A sample MicroPython appliction for a Raspberry Pico. 
"""

from machine import Pin, RTC
import utime
import sys

from board import name as board_name

_author = 'Cees van de Griend <cees@griend.eu>'
_name = 'blink'
_version = 'v0.1'

rtc = RTC()
led = Pin(25, Pin.OUT)
light = 0


def light_on():
    global rtc, led, light

    now = rtc.datetime()
    light = 1
    print(f'{now[0]:04n}-{now[1]:02n}-{now[2]:02n} {now[4]:02n}:{now[5]:02n}:{now[6]:02n} - Light: {light}')
    
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(0.5)
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(0.5)
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(0.5)
    led.value(1)
    utime.sleep(5.0)
    led.value(0)

    now = rtc.datetime()
    light = 0
    print(f'{now[0]:04n}-{now[1]:02n}-{now[2]:02n} {now[4]:02n}:{now[5]:02n}:{now[6]:02n} - Light: {light}')


def light_off():
    global led, light

    light = 0
    led.value(0)


def info():
    print(f'''
Board:   {board_name}
Author:  {_author}
Version: {_name} / {_version}

Light:   {light}
''')


def main():
    while True:
        light_on()
        utime.sleep(8.0)


if __name__ == '__main__':
    info()
    main()    

