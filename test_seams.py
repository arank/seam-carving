import image



im = image.sc_Image.from_filepath2("images/comet.jpg")

im.to_seam_pic("images/comet_seams_kroon.jpg",50, energy = 'kroon')