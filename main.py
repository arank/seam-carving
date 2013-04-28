import image

im = image.sc_Image.from_filepath2("castle.jpg")

im.shrink(100, alg = 'dyn')
# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("new_castle2.jpg")

