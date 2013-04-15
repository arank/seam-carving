#run this to make sure Python Imaging Library and libjpeg are installed correctly

import Image

im = Image.open ("castle.jpg")

print im.format, im.size, im.mode

print list(im.getdata())