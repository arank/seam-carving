# calculates the lowest horizontal seam starting at a given pixel with Dijkstra's
def seam_hor_dijk (image, pixel) :
	return seam

# calculates the lowest horizontal seam starting at a given pixel with dynamic programming
def seam_hor_dyn (image, pixel) :
	return seam


def seam_vert_dijk (image, pixel) :
	return seam

def seam_vert_dyn (image, pixel) :
	return seam

# If resize is vertical, then calls seam_for_start_vert on every 
# pixel at the left edge of the image and finds the lowest.
# If resize is horizontal, then calls seam_for_start_hor on every
# pixel at the top edge of the image and finds the lowest.
# This looks dumb; we'll find a way to fix it later.
def seam_finder (image, dir, alg) :
	if dir = 'hor' :
		if alg = 'dijk' :
			lowest = seam_hor_dijk(image, get_pixel((0,0)))
			for h in range(image.height):
				let testseam = seam_hor_dijk(image, get_pixel((0,h)))
				if testseam.energy < lowest.energy :
					lowest = testseam
			return lowest
		else :
			lowest = seam_hor_dyn(image, get_pixel((0,0)))
			for h in range(image.height):
				let testseam = seam_hor_dyn(image, get_pixel((0,h)))
				if testseam.energy < lowest.energy :
					lowest = testseam
			return lowest
	else :
		if alg = 'dijk' :
			lowest = seam_vert_dijk(image, get_pixel((0,0)))
			for h in range(image.width):
				let testseam = seam_vert_dijk(image, get_pixel((w,0)))
				if testseam.energy < lowest.energy :
					lowest = testseam
			return lowest
		else :
			lowest = seam_vert_dyn(image, get_pixel((0,0)))
			for h in range(image.width):
				let testseam = seam_vert_dyn(image, get_pixel((w,0)))
				if testseam.energy < lowest.energy :
					lowest = testseam
			return lowest

# removes finalseam from image.
class Seam :
	def__init__(self, pixels) :
		self.pixels = pixels
		self.energy = energy
		self.removed = false

	def seam_remover (seam, image) :
		removed = true
		raise NotImplementedError
		return newimage




