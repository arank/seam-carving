import image

im = image.sc_Image.from_filepath2("dolphin.jpg")

im.to_energy_pic('skateboarder_energy2.jpg')
im.shrink(50, alg = 'dyn', orientation = 'horizontal')
im.to_energy_pic('dolphin_energy2.jpg')
im.shrink(50, alg = 'dyn')
# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("dolphin_kroon.jpg")


