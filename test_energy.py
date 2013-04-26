import image

im = image.sc_Image.from_filepath2("skateboarder.jpg")

im.set_energies('e1')

im.to_energy_pic("new_energy_skateboarder.jpg")

