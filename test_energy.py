import image

im = image.sc_Image.from_filepath2("images/skateboarder.jpg")


im.to_energy_pic("images/entropy_skateboarder.jpg", 'entropy')

