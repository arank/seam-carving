import image

# a fucntion other than main that we can use for top level testing of indavidual subprocessess
# in this case seams with the dynamic algorithm reprsented by the higlighted seam picture printed out

im = image.sc_Image.from_filepath2("images/comet.jpg")

im.to_seam_pic("images/comet_seams_kroon.jpg",50, energy = 'kroon')