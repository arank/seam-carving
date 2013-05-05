from PIL import Image
'''
	simple testing for the Python imageing library
	run this to ensure that the library is operating as expected
'''

img = Image.open ("castle.jpg")
print ('this is the RGBA of (0,0): %r' % img[0,0])
