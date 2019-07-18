from microbit import *
import neopixel

np = neopixel.NeoPixel(pin1, 12)

red = (50, 0, 0)
orange = (50, 25, 0)
yellow = (40, 50, 0)
green = (0, 50, 0)
blue = (0, 0, 50)
indigo = (50, 0, 25)
violet = (50, 0, 50)
white = (50, 50, 50)

colours = [red, red, orange, orange, yellow, yellow,
           green, green, blue, blue, violet, violet]

off = False
duck = True

while True:
    while off is False:
        for pixel in range(0, len(np)):
            np[pixel] = colours[pixel]
        np.show()
        for x in range(0, 2):
            colours.append(colours.pop(0))
        sleep(500)
        if duck == True:
            display.show(Image.DUCK)
            duck = False
        elif duck == False:
            display.clear()
            duck = True
        if button_a.was_pressed():
            off = True
            np.clear()
            display.show(Image.GIRAFFE)
    if button_a.was_pressed():
            off = False
