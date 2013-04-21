import image

im = image.sc_Image.from_filepath2("castle.jpg")

print im.pixels[(1500,0)]

# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("new_castle.jpg")

