from energy import e1, entropy

import Image



#representation of image for seam carving
class sc_Image
    def __init__(self, dimensions, pixels): 
    	self.width = dimensions[0]
    	self.height = dimensions[1]
    	self.dimensions = dimensions
    	self.pixels = pixels
    	self.seams = []

    #loop through the pixels and set all of their energy values
    def calculate_energies(self, algorithm) :
    	for h in range(height):
			for w in range(width):
				pixels[(w,h)].energy = get_energy((w,h), algorithm)


    # get the neighbors of the pixel at pos
    def get_neighbors (self, pos):
    	raise NotImplementedError

    # gets the 9x9 square of pixels of the pixel at pos
    def get_square (self, pos):
    	raise NotImplementedError

    def get_pixel(self, pos):
    	if pos in self.pixels:
    		return self.pixels[pos]
    	else:
    		return None

    # gets the energy of the pixel at a position
    def get_energy (self, pos, algorithm) :
		if algorithm == 'e1':
			map (lambda x: e1 (x, get_neighbors(x) ), self.pixels.values ) 

		elif algorithm == 'entropy':
			map (lambda x: entropy (x,  get_square(x) ), self.pixels.values ) 

		else:
			raise Exception("%s is not one of the implemented algorithms" % algorithm)


	#write a jpeg representation of this image to a file
	def to_jpeg(self, filepath):
		raise NotImplementedError

class Pixel:
    def __init__(self, pos, rgb): 
    	self.pos = pos
    	self.rgb = rgb
    	self.energy = -1

    # to string function
    def __str__(self):
        return "[%s - %s]" % (str(self.pos), str(self.rgb))

#given an image file turns into an sc_Image class
def data_from_image(filepath):
	pixels = {}
	im = Image.open (filepath)
	width, height = im.size
	for h in range(height):
		for w in range(width):
			pixels[(w,h)] = Pixel( (w,h), im.getpixel((w,h)) )
	return sc_Image((width, height), pixels)


