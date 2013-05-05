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

# im = image.sc_Image.from_filepath("images/castle.jpg")
# im.to_energy_pic('images/castle_sobel.jpg', 'sobel')
# im.to_energy_pic('images/castle_scharr.jpg', 'scharr')
# im.to_energy_pic('images/castle_kroon.jpg', 'kroon')
# im.to_energy_pic('images/castle_sobel5.jpg', 'sobel5')
# im.to_energy_pic('images/castle_scharr5.jpg', 'scharr5')

# Object enlarement on the sun

# im = image.sc_Image.from_filepath("images/sunset.jpeg")
# im.enlarge_object_1d(40, orientation = 'horizontal')
# im.enlarge_object_1d(40, orientation = 'vertical')


# im.to_jpeg("images/big_sunset.jpg")

# Removes the colored skateboarder and dolphin from the respecitve images

# im = image.sc_Image.from_filepath("images/skateboarder_to_remove.jpg")
# im.remove_object((35, 255, 9), 5)
# im.to_jpeg("images/skateboarder_object_removed.jpg")


# im = image.sc_Image.from_filepath("images/dolphin_to_remove.jpg")
# im.remove_object((35, 255, 9), 5)
# im.to_jpeg("images/dolphin_object_removed.jpg")

# Content aware resizes intermediate image

# im = image.sc_Image.from_filepath("images/intermediate.jpg")
# im.enlarge(54)
# im.to_jpeg("images/sunset_removed.jpg")

# Gives the highligheted seams picure when 80 seams are removed with entropy energy finding
# as well as shrinks the image.

# im.to_seam_pic("images/skateboarder_entropy_seams.jpg",80, energy = 'entropy')

#im.shrink(30,energy = 'sobel', alg = 'dyn')

#im.to_jpeg("images/castle_small.jpg")



#enlarging landscape.jpg by 50 seams

im = image.sc_Image.from_filepath("images/landscape.jpg")
im.enlarge(1 ,orientation = 'horizontal', energy = 'sobel', alg = 'dyn')
im.to_jpeg("images/landscape_enlarged.jpg")

#enlarging skateboarder by 80 pixels

# im = image.sc_Image.from_filepath("images/skateboarder.jpg")
# im.enlarge(80,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("images/skateboarder_enlarged.jpg")

#enlargin plane by 80 pixels

# im = image.sc_Image.from_filepath("images/red_plane.jpg")
# im.enlarge(80,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("images/red_plane_enlarged.jpg")

#shrinking sunset by 60 pixels

# im = image.sc_Image.from_filepath("images/sunset.jpeg")
# im.shrink(60,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("images/sunset_shrank.jpg")

#shrinking dolphin by 60 pixels
#some of his fin is cut off because it is similar in color to the sky

# im = image.sc_Image.from_filepath("images/dolphin.jpg")
# im.shrink(60,orientation = 'vertical', energy = 'sobel5', alg = 'dyn')
# im.to_jpeg("images/dolphin_shrank.jpg")

