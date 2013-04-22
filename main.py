import image

im = image.sc_Image.from_filepath2("skateboarder.jpg")

im.shrink(80)
# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("new_skateboarder.jpg")

