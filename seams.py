class Seam :
	def __init__ (self, pixels) :
		self.pixels = pixels
		self.energy = energy
		self.removed = false


# calculates the lowest seam starting at a given pixel with Dijkstra's
#helper methods may be added later
class Heap :
	def __init__():

	#adds edge to heap and fixes it
	def add (edge):

	#gets top value, and removes it from heap, fixing heap afterwards
    def get_top () :


class Edge :
	def __init__(source, sink, weight):


def seam_dijk (image, dir) :
	super_source = None

	def get_path(edge, path) :
		path.append(edge.sink)
		if edge.source == super_source :
			return path
		else :
			get_path(edge.source, path)

	for pix in image.top_vert_row(): #also do top horz rowm
		heap.add(Edge(super_source, pix, pix.energy))

	while True :
		edge = heap.get_top()

		if edge.sink.y == (image.height-1) :
			return get_path(edge,[])

		down =image.pixels[ (edge.sink.x, (edge.sink.y+1)) ]
		heap.add(Edge(edge, down, down.energy+edge.weight))

		if edge.sink.x == (image.width-1) :
			left = image.pixels[ ((edge.sink.x-1), (edge.sink.y+1)) ]
			heap.add(Edge(edge, left, left.energy+edge.weight))

		elif edge.sink.x == 0 :
			right = image.pixels[ ((edge.sink.x+1), (edge.sink.y+1)) ]
			heap.add(Edge(edge, right, right.energy+edge.weight))	
		else :
			left = image.pixels[ ((edge.sink.x-1), (edge.sink.y+1)) ]
			right = image.pixels[ ((edge.sink.x+1), (edge.sink.y+1)) ]
			heap.add(Edge(edge, right, right.energy+edge.weight))	
			heap.add(Edge(edge, left, left.energy+edge.weight))	




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
	# 		testseam = s9oeam_dijk(image, get_pixel(pos))
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






