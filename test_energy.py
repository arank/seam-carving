import image

im = image.sc_Image.from_filepath2("landscape.jpg")

im.set_energies('e1')

im.to_energy_pic("new_energy_landscape.jpg")

