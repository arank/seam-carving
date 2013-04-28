import image

#The following strings may be used for energy calculation:
#'sobel', 'scharr', 'kroon', 'sobel5', 'scharr5'
#The 'entropy' call may be used as well but will not work
#as of right now. Its glitch will be fixed in the next code update


im = image.sc_Image.from_filepath2("landscape.jpg")

im.to_energy_pic('landscape_entropy.jpg', 'entropy')

im.enlarge(80, alg = 'dyn', energy = "entropy", orientation = 'horizontal')

image.shrink( 'horizontal', 300 , 'e1', 'dyn')



im.to_jpeg("dolphin_horizontal_enlarge.jpg")




#enlarging skateboarder by 80 pixels

im = image.sc_Image.from_filepath2("skateboarder.jpg")
im.enlarge(80,orientation = 'horizontal', energy = 'e1', alg = 'dyn')
im.to_jpeg("skateboarder_enlarged.jpg")
