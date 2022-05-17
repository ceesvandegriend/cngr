"""
Name:        blink
Author:      Cees van de Griend <cees@griend.eu>
Date:        2022-05-13

Description: A sample MicroPython appliction for a Raspberry Pico. 
"""

from machine import Pin, Timer

import sys
import select
import time


_debug_ = False

line = ''

led = Pin(25, Pin.OUT)
blink_msec = 500
timer = Timer()

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)


def _read():
    return(sys.stdin.read(1) if poll.poll(0) else None)


def readln():
    global line

    eol = False
    ch = _read()

    if (ch):
        if (ch) == '\n':
            eol = True
        else:
            line += ch

    return eol



def blink(timer):
    global led

    if _debug_:
        print('** Blinking **')

    led.value(1)
    time.sleep_ms(blink_msec)
    led.value(0)

    if _debug_:
        print('** Blinked **')


def help():
    if _debug_:
        print('** Helping **')

    """ Simple print a help message. """
    print('''---------
  Blink:

    debug - toggle debug information
    help  - this help messag
    off   - turn blink off
    on    - turn blink on
    quit  - stop the application
---------''')

    if _debug_:
        print('** Helped **')


def off():
    """
    Simple function to switch the LED off.
    """
    global led

    if _debug_:
        print('** Switching off **')

    timer.deinit()
    print('Blink off')

    if _debug_:
        print('** Switched off **')



def on():
    """
    Simple function to switch the LED on.
    """
    global led
    
    if _debug_:
        print('** Switching on **')

    timer.init(mode = Timer.PERIODIC, period=blink_msec * 2, callback=blink)
    print('Blink on')

    if _debug_:
        print('** Switched on **')


def main():
    """
    Main loop.
    """
    global _debug_
    global line
    global led

    stopping = False
    on()

    while not stopping:
        if (readln()):
            if _debug_:
                print(f'> {line}')

            # Handle commands
            if line == 'debug':
                _debug_ = not _debug_
                print(f'Debug: {_debug_}')
            elif line == 'help':
                help()
            elif line == 'off':
                off()
            elif line == 'on':
                on()
            elif line == 'quit':
                if _debug_:
                    print('** Stopping **')
                stopping = True
                print('Quit')
            else:
                print(f'** Unknown command: {line}')

            # Asume we are done
            line = ''
        else:
            time.sleep(0.1)

    if _debug_:
        print('** Stopped **')
    

if __name__ == '__main__':
    main()
