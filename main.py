import image


#The following strings may be used for the energy argument:
#'sobel', 'scharr', 'kroon', 'sobel5', 'scharr5'


#The 'entropy' call may be used as well but will not work
#as of right now. Its glitch will be fixed in the next code update

#The following strings may be used for seam derivation (the alg argument):
#'dyn', 'dijk'

# The following strings can be used can be used for the orientation argument:
# 'vertical' or 'horizontal'
# denoting vertical or horizontal seams


# Usage examples:


#Energy Maps
#==================#

# Creating several energy maps of castle image

# im = image.sc_Image.from_filepath("images/castle.jpg")
# im.to_energy_pic('images/castle_sobel5.jpg', 'sobel5')
# im.to_energy_pic('images/castle_scharr5.jpg', 'scharr5')
# im.to_energy_pic('images/castle_sobel.jpg', 'sobel')
# im.to_energy_pic('images/castle_scharr.jpg', 'scharr')
# im.to_energy_pic('images/castle_kroon.jpg', 'kroon')
# im.to_energy_pic('images/castle_entropy.jpg', 'entropy')

# Displays the energy maps for giza
# im = image.sc_Image.from_filepath("images/giza.jpg")
# im.to_energy_pic('images/energy_map_entropy.jpg', 'entropy')
# im.to_energy_pic('images/energy_map_sobel.jpg', 'sobel')
# im.to_energy_pic('images/energy_map_kroon.jpg', 'kroon')
# im.to_energy_pic('images/energy_map_sobel5.jpg', 'sobel5')
# im.to_energy_pic('images/energy_map_scharr5.jpg', 'scharr5')


#Image Shrinking
#==================#

# Shrinks night by 120 pixels in the vertical direciton by removing horizontal seams

# im = image.sc_Image.from_filepath("images/night.jpg")
# im.shrink(120,orientation = 'horizontal', energy = 'scharr', alg = 'dyn')
# im.to_jpeg("images/night_shrank.jpg")


#shrinking sunset by 60 pixels

# im = image.sc_Image.from_filepath("images/sunset.jpeg")
# im.shrink(60,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("images/sunset_shrank.jpg")

#shrinking dolphin by 60 pixels
#some of his fin is cut off because it is similar in color to the sky

# im = image.sc_Image.from_filepath("images/dolphin.jpg")
# im.shrink(60,orientation = 'vertical', energy = 'sobel5', alg = 'dyn')
# im.to_jpeg("images/dolphin_shrank.jpg")

#shrinking birds by 120 pixels

# im = image.sc_Image.from_filepath("images/birds.jpg")
# im.shrink(180,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("images/birds_shrank.jpg")

#shrinking stones by 120 pixels

# im = image.sc_Image.from_filepath("images/stones.jpg")
# im.shrink(120,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("images/stones_shrank.jpg")

#shrinking giza by 120 pixels

# im = image.sc_Image.from_filepath("images/giza.jpg")
# im.shrink(120,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("images/giza_shrank.jpg")


#Image Enlargement
#==================#

# Enlarges landscape.jpg by 50 seams

# im = image.sc_Image.from_filepath("images/landscape.jpg")
# im.enlarge(50,orientation = 'vertical', energy = 'kroon', alg = 'dyn')
# im.to_jpeg("images/landscape_enlarged.jpg")

#enlarging skateboarder by 80 pixels

# im = image.sc_Image.from_filepath("images/skateboarder.jpg")
# im.enlarge(80,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("images/skateboarder_enlarged.jpg")

#enlarging plane by 80 pixels

# im = image.sc_Image.from_filepath("images/red_plane.jpg")
# im.enlarge(80,orientation = 'vertical', energy = 'sobel', alg = 'dyn')
# im.to_jpeg("images/red_plane_enlarged.jpg")


#Object removal
#==================#

# Removes the colored-in skateboarder from the skateboarder image

# im = image.sc_Image.from_filepath("images/skateboarder_to_remove.jpg")
# im.remove_object((35, 255, 9), 5)
# im.to_jpeg("images/skateboarder_object_removed.jpg")


# Removes the colored-in dolphin from the dolphin image

# im = image.sc_Image.from_filepath("images/dolphin_to_remove.jpg")
# im.remove_object((35, 255, 9), 5)
# im.to_jpeg("images/dolphin_object_removed.jpg")


# Removes the colored-in dolphin from the sunset image

# im = image.sc_Image.from_filepath("images/sunset_to_remove.jpg")
# im.remove_object((35, 255, 9), 5)
# im.to_jpeg("images/sunset_object_removed.jpg")


#Seam Pictures
#==================#

# #displays seams created by sobel
# im = image.sc_Image.from_filepath("images/giza.jpg")
# im.to_seam_pic("images/sobel.jpg",80, energy = 'sobel')

#displays seams created by scharr
# im = image.sc_Image.from_filepath("images/giza.jpg")
# im.to_seam_pic("images/scharr.jpg",80, energy = 'scharr')

# #displays seams created by kroon
# im = image.sc_Image.from_filepath("images/giza.jpg")
# im.to_seam_pic("images/kroon.jpg",80, energy = 'kroon')

#displays seams created by scharr5
# im = image.sc_Image.from_filepath("images/giza.jpg")
# im.to_seam_pic("images/scharr5.jpg",80, energy = 'scharr5')

#horiztonal seam picture for night
# im = image.sc_Image.from_filepath("images/night.jpg")
# im.to_seam_pic("images/night_seams.jpg", 120,orientation = 'horizontal', energy = 'scharr', alg = 'dyn')

#displays seams found by dijkstra's algorithm
# im = image.sc_Image.from_filepath("images/landscape.jpg")
# im.to_seam_pic("images/dijk_seams.jpg",10, energy = 'sobel', alg = 'dijk')

#displays seams found by dynamic programming
# im = image.sc_Image.from_filepath("images/landscape.jpg")
# im.to_seam_pic("images/dyn_seams.jpg",10, energy = 'sobel', alg = 'dyn')

#Object enlargement
#==================#

# im = image.sc_Image.from_filepath("images/skateboarder.jpg")
# im.enlarge_object_1d(40)
# im.to_jpeg("images/skateboarder_1D_enlarged.jpg")


