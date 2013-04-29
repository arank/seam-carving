import image

#The following strings may be used for the energy argument:
#'sobel', 'scharr', 'kroon', 'sobel5', 'scharr5'


#The 'entropy' call may be used as well but will not work
#as of right now. Its glitch will be fixed in the next code update

#The following strings may be used for seam derivation (the alg argument):
#'dyn', 'dijk'

#The following strings can be used can be used for the orientation argument:
# 'vertical' or 'horizontal'
#denoting vertical or horizontal seams


#Usage examples:

#Creating several energy maps of castle image

# im = image.sc_Image.from_filepath2("castle.jpg")
# im.to_energy_pic('castle_sobel.jpg', 'sobel')
# im.to_energy_pic('castle_scharr.jpg', 'scharr')
# im.to_energy_pic('castle_kroon.jpg', 'kroon')
# im.to_energy_pic('castle_sobel5.jpg', 'sobel5')
# im.to_energy_pic('castle_scharr5.jpg', 'scharr5')


#enlarging landscape.jpg by 50 seams

# im = image.sc_Image.from_filepath2("landscape.jpg")
# im.enlarge(50 ,orientation = 'horizontal', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("landscape_enlarged.jpg")

#enlarging skateboarder by 80 pixels

# im = image.sc_Image.from_filepath2("skateboarder.jpg")
# im.enlarge(80,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("skateboarder_enlarged.jpg")

#enlargin plane by 80 pixels

# im = image.sc_Image.from_filepath2("red_plane.jpg")
# im.enlarge(80,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("red_plane_enlarged.jpg")

#shrinking sunset by 60 pixels

# im = image.sc_Image.from_filepath2("sunset.jpeg")
# im.shrink(60,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("sunset_shrank.jpg")

#shrinking dolphin by 60 pixels
#some of his fin is cut off because it is similar in color to the sky

# im = image.sc_Image.from_filepath2("dolphin.jpg")
# im.shrink(60,orientation = 'vertical', energy = 'sobel5', alg = 'dyn')
# im.to_jpeg("dolphin_shrank.jpg")

