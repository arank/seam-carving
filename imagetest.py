from PIL import Image

img = Image.open ("castle.jpg")
print ('this is the RGBA of (0,0): %r' % img[0,0])
