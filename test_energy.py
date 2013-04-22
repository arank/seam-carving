import image

im = image.sc_Image.from_filepath2("castle.jpg")

im.set_energies('e1')

for w in range(40):
	for h in range(40):
		print str( im.pixels[(w,h)])


im.to_jpeg("new_castle.jpg")

