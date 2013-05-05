# a fucntion other than main that we can use for top level testing of indavidual subprocessess
# in this case energy finding with energy and the heat map

import image

im = image.sc_Image.from_filepath2("images/skateboarder.jpg")


im.to_energy_pic("images/entropy_skateboarder.jpg", 'entropy')

