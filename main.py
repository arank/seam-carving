import image

im = image.sc_Image.from_filepath2("dolphin.jpg")

im.to_energy_pic('skateboarder_energy2.jpg')
im.shrink(50, alg = 'dyn', orientation = 'horizontal')
# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("dolphin2.jpg")


