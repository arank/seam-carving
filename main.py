import image

im = image.sc_Image.from_filepath2("landscape.jpg")

#im.to_energy_pic('skateboarder_energy2.jpg')
#im.shrink(50, alg = 'dyn', orientation = 'horizontal')
im.to_energy_pic('landscape_energy.jpg')
im.shrink(1, alg = 'dyn', energy = "entropy")
# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("dolphin_kroon.jpg")



