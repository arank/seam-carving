import image



im = image.sc_Image.from_filepath2("dolphin.jpg")

im.to_energy_pic('dolphin_energy.jpg')

im.enlarge(80, alg = 'dyn', energy = "e1", orientation = 'horizontal')

# image.shrink( 'horizontal', 300 , 'e1', 'dyn')



im.to_jpeg("dolphin_horizontal_enlarge.jpg")

