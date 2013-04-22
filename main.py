import image

im = image.sc_Image.from_filepath2("landscape.jpg")


# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_energy_pic("new_landscape.jpg")

