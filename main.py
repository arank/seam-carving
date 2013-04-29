import image



im = image.sc_Image.from_filepath2("dolphin.jpg")

im.to_energy_pic('dolphin_energy.jpg')

im.enlarge(80, alg = 'dyn', energy = "e1", orientation = 'horizontal')

# image.shrink( 'horizontal', 300 , 'e1', 'dyn')



im.to_jpeg("dolphin_horizontal_enlarge.jpg")




#enlarging skateboarder by 80 pixels

im = image.sc_Image.from_filepath2("skateboarder.jpg")
im.enlarge(80,orientation = 'horizontal', energy = 'e1', alg = 'dyn')
im.to_jpeg("skateboarder_enlarged.jpg")
