import image

im = image.sc_Image.from_filepath("castle.jpg")

# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("new_castle.jpg")

