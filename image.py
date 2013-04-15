from energy import e1, entropy
from seams import Seam, seam_dijk, seam_dyn

import Image



#representation of an image for seam carving
class sc_Image
    def __init__(self, dimensions, pixels): 
    	self.width = dimensions[0]
    	self.height = dimensions[1]
    	self.dimensions = dimensions
    	self.pixels = pixels

    #loop through the pixels and set all of their energy values
    def calculate_energies(self, algorithm) :
    	for h in range(height):
			for w in range(width):
				pixels[(w,h)].energy = get_energy((w,h), algorithm)


    # get the neighbors of the pixel at pos for e1 function
    def get_neighbors (self, pos):
    	raise NotImplementedError

    # gets the 9x9 square of pixels of the pixel at pos for entropy function
    def get_square (self, pos):
    	raise NotImplementedError

    def get_pixel(self, pos):
    	if pos in self.pixels:
    		return self.pixels[pos]
    	else:
    		return None

    # sets the energies
    def set_energies (self, algorithm) :
		if algorithm == 'e1':
			map (lambda p: e1 (p, self.get_neighbors(p) ), self.pixels.values ) 

		elif algorithm == 'entropy':
			map (lambda p: entropy (p,  self.get_square(p) ), self.pixels.values ) 

		else:
			raise Exception("%s is not one of the implemented algorithms" % algorithm)

	# If resize is vertical, then calls seam_for_start_vert on every 
	# pixel at the left edge of the image and finds the lowest.
	# If resize is horizontal, then calls seam_for_start_hor on every
	# pixel at the top edge of the image and finds the lowest.
	def get_next_seam (self, alg = 'dyn', orientation = 'horizontal') :

		if orientation ='vertical' : 
			pixels = map (self.get_pixel, [(0,h) for h in range(self.height)] )
		elif orientation = 'horizontal'
			pixels = map (self.get_pixel, [(w,0) for w in range(self.width)] )
		else:
			raise Exception("Orientation must be vertical or horizontal" )

		#create a list of seam objects
		if alg= 'dijk': 
			seams = map (seam_dijk, self.pixels)
		elif alg = 'dyn' :
			seams = map (seam_dyn, self.pixels)
		else:
			raise Exception("%s is not one of the implemented algorithms" % algorithm)


		#write a jpeg representation of this image to a file
		def to_jpeg(self, filepath):
			raise NotImplementedError

	#removes a seam from the image
	def remove_seam (self, seam) :
		raise NotImplementedError

	#
	def enlarge (self, orientation, new_pixels, energy = 'e1', seam = 'dyn'):
		raise NotImplementedError

	#
	def shrink (self, orientation, new_pixels, energy = 'e1', seam = 'dyn'):
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


