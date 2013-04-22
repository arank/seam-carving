import image

im = image.sc_Image.from_filepath2("castle.jpg")

im.set_energies('e1')

im.to_energy_pic("energy_castle.jpg")

