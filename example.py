from machine import Pin, SPI
import time
import max7219

NUM_SEGMENTS = 4

spi = SPI(1, baudrate=10_000_000, polarity=0, phase=0)
display = max7219.Matrix8x8(spi, cs=Pin(15), num=NUM_SEGMENTS, extended=True)

display.brightness(0)

scrolltext = "     Hello World!"

while True:
    for i in range(len(scrolltext)-1):
        display.fill(0)
        display.text(scrolltext[i:i+6], 0 ,1)
        display.show()
        for j in range(8):
            time.sleep(.07)
            display.scroll(-1,0)
            display.show()
