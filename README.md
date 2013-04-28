seam-carving
============

Seam Carving (CS51 Project)

Our project is implemented in the form of a class, sc_Image (seam-carving image).

To use our seam carving methods on image, the first step is creating an sc_Image object. 

The constructor for sc_Image takes the filepath of a an image file. Here is an example of how to create
a sc_Image object: 

im = image.sc_Image.from_filepath2("comet.jpg")

Once an sc_Image has been created, we have some public methods to use to resize the image using 
seam carving. 

sc_Image.shrink(to_remove, orientation = "vertical", energy = 'e1', alg = 'dijk')

Makes the image smaller by removing "to_remove" columns or rows of pixels. 

Where "to_remove" is the number of pixels to shrink by, "orientation" is the dimension to shrink the image in 
(must be "horizontal" or "vertical"), "energy" is an optional argument specifying the energy calculation to use
(defaults to "e1", the other option is "e1_five", "entropy" will be implemented by next week), and "alg" is the seam 
finding algorithm to use (options are "dyn" for dynamic programming and "dijk" for Dijkstra's algorithm).


sc_Image.enlarge(new_pixels, orientation = 'vertical', energy = 'e1', alg = 'dyn')

Where new_pixels is the number of pixels to add, orientation is the dimension to add them in ("horizontal" or "vertical"),
"energy" is an optional argument specifying the energy calculation to use
(defaults to "e1", the other option is "e1_five", "entropy" will be implemented by next week), and "alg" is the seam 
finding algorithm to use (options are "dyn" for dynamic programming and "dijk" for Dijkstra's algorithm).



Once the image has been resized, it can be outputted back to an image file using the sc_Image.to_jpeg(filepath) method where filepath
is the file location to save the new image.