import image

im = image.sc_Image.from_filepath2("castle.jpg")

print [str(p) for p in im.get_next_seam("dijk")]

# image.shrink( 'horizontal', 300 , 'e1', 'dyn')

im.to_jpeg("new_castle.jpg")

