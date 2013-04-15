class Seam :
	def__init__(self, pixels) :
		self.pixels = pixels
		self.energy = energy
		self.removed = false


# calculates the lowest seam starting at a given pixel with Dijkstra's
#helper methods may be added later
def seam_dijk (image, pixel, dir) :
	raise NotImplementedError
	return seam

# calculates the lowest seam starting at a given pixel with dynamic programming
#helper methods may be added later
def seam_dyn (image, pixel, dir) :
	raise NotImplementedError
	return seam



# This looks dumb; we'll find a way to fix it later.
#old def seam_finder(image, alg, dir) :
	# if dir = 'vert' : row_length = image.height
	# else : row_length = image.width

	# if alg = 'dijk' :
	# 	lowest = seam_dijk(image, get_pixel((0,0)), dir)
	# 	for l in range(row_length):
	# 		if dir == 'vert' : pos = (0,l) 
	# 		else : pos = (l,0)
	# 		testseam = seam_dijk(image, get_pixel(pos))
	# 		if testseam.energy < lowest.energy :
	# 			lowest = testseam
	# else :
	# 	lowest = seam_dyn(image, get_pixel((0,0)))
	# 	for l in range(row_length):
	# 		if dir == 'vert' : pos = (0,l) 
	# 		else : pos = (l,0)
	# 		testseam = seam_dyn(image, get_pixel(pos))
	# 		if testseam.energy < lowest.energy :
	# 			lowest = testseam
	# return lowest






