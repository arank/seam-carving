import image

image = data_from_image("castle.jpg")

image.enlarge( 'horizontal', 300 , 'e1', 'dyn')

image.to_jpeg("new_castle.jpg")

