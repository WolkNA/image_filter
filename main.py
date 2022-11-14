from PIL import Image
import os, sys
import random


fname = './Dune.bmp'


def img_uproar(fname, uproar):
    with Image.open(fname) as image:
        pixels = image.load()
        width = image.size[0]
        height = image.size[1]
        size = width*height
        uproar_size = int((size * uproar)/100)
        for i in range(0,uproar_size):
            x = random.randint(0,width-1)
            y = random.randint(0,height-1)
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            pixels[x,y] = (red, green, blue)
    image.show()
    image.save('./uproar.bmp')

def filter(fname, channel = 0):
    with Image.open(fname) as image:
        pixels = image.load()
        width = image.size[0]
        height = image.size[1]
        for h in range(1, height-2):
            for w in range(1,width-2):
                list = []
                mod_list = []
                for i in range(0,3):
                    for j in range(0,3):
                        list.append(pixels[w+j,h+i][channel])
                        mod_list.append(pixels[w+j,h+i][channel])
                mod_list.sort()
                list[4] = mod_list[4]
                red = pixels[w+1,h+1][0]
                green = pixels[w+1,h+1][1]
                blue = pixels[w+1,h+1][2]
                if channel == 0:
                    red = list[4]
                elif channel == 1:
                    green=list[4]
                elif channel ==2:
                    blue = list[4]
                (pixels[w+1,h+1]) = (red, green, blue)
    image.show()
    image.save('./median.bmp')

uproar = input('Input uproar: ')
try: uproar = int(uproar)
except: uproar = 0

if uproar <0: uproar = 0
#elif uproar > 100: uproar = 100


img_uproar(fname, uproar)

filter('./uproar.bmp', 0)
filter('./median.bmp', 1)
filter('./median.bmp', 2)
