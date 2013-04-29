import image

#The following strings may be used for energy calculation:
#'sobel', 'scharr', 'kroon', 'sobel5', 'scharr5'
#The 'entropy' call may be used as well but will not work
#as of right now. Its glitch will be fixed in the next code update

#The following strings may be used for seam derivation:
#'dyn', 'dijk'

#Creating several energy maps of castle image
im = image.sc_Image.from_filepath2("castle.jpg")
im.to_energy_pic('castle_sobel.jpg', 'sobel')
im.to_energy_pic('castle_scharr.jpg', 'scharr')
im.to_energy_pic('castle_kroon.jpg', 'kroon')
im.to_energy_pic('castle_sobel5.jpg', 'sobel5')
im.to_energy_pic('castle_scharr5.jpg', 'scharr5')

#shrinking landscape by 50 seams
im = image.sc_Image.from_filepath2("landscape.jpg")
im.enlarge(50 ,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
im.to_jpeg("small_landscape.jpg")

#enlarging skateboarder by 80 pixels
im = image.sc_Image.from_filepath2("skateboarder.jpg")
im.enlarge(80,orientation = 'horizontal', energy = 'sobel', alg = 'dyn')
im.to_jpeg("skateboarder_enlarged.jpg")
#orientation can be 'vertical' or 'horizontal'




