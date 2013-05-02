import image



im = image.sc_Image.from_filepath2("images/landscape.jpg")

im.to_seam_pic("images/landscape_seams_krron.jpg",50, energy = 'kroon')