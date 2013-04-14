import Image

im = Image.open ("castle.jpg")

print im.format, im.size, im.mode

print list(im.getdata())