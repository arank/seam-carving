import image

im = image.sc_Image.from_filepath2("images/landscape.jpg")


im.to_energy_pic("images/entropy_landscape.jpg", 'entropy')

