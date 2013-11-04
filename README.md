seam-carving
Seam Carving (CS51 Project)

By: Aran Khanna, Andrew Maubossin, Sergui Balanovich

Dependency: Python Imaging Library (PIL)

A Python library to perform content-aware image resizing methods like image scaling and object removal using seam carving. Check out the images folder for some examples.

To run: Edit main.py to specify the seam carving operations to be performed. Example code is provided in the file and test images are in the data folder. Then execute main.py ("python main.py" in a unix shell).

Our project is implemented in the form of a class, sc_Image (seam-carving image).

To use our seam carving methods on image, the first step is creating an sc_Image object. The constructor for sc_Image takes the filepath of a an image file. Here is an example of how to create an sc_Image object:

-->im = image.sc_Image.from_filepath("comet.jpg")

Once an sc_Image has been created, we have some public methods to use to resize the image using seam carving:

-->sc_Image.shrink(to_remove, orientation = "vertical", energy = 'e1', alg = 'dijk') Shrinks an image in one direction. *to_remove (int): the number of pixels to be removed from the image. *orientation (string): the direction the seams run in. The two options are 'vertical' and 'horizontal'. Vertical will alter the image's width and horizontal will change its height. *energy (string): the energy function to be applied to the image. The options are 'sobel' 'scharr' 'kroon' 'sobel5' 'scharr5' and 'entropy'. The first three use 3x3 pixel filters with varying weights. The next two use 5x5 pixel filters. The final one uses a 9x9 histogram to calculate the entropy of a every pixel. Be aware that the first three will run more quickly than the others. *alg (string): the shortest path algorithm to be used. The two options are 'dijk' and 'dyn'. Be aware that dijkstra's doesn't work with enlarge or remove object due to the way it deals with negative energy values.

-->sc_Image.enlarge(new_pixels, orientation = 'vertical', energy = '', alg = 'dyn') Enlarges an image in one direction. *new_pixels (int): the number of pixels to be added to the image. *orientation (string): Same options and functionality as shrink. *energy (string): '...' *alg (string): '...'

-->sc_Image.enlarge_object_1d(new_pixels, orientation="vertical", energy='sobel', alg='dyn') Enlarges high-energy objects in one dimension while retaining the size of the original photo. *new_pixels (int): the number of pixels by which high energy objects should be enlarged. *orientation (string): '...' *energy (string): '...' *alg (string): '...'

-->sc_Image.enlarge_object(seams, energy = 'sobel', alg = 'dyn') Enlarges high-energy objects in two dimensions. *seams (int): the number of seams by which high energy objects should be enlarged *energy (string): '...' *alg (string); '...'

-->sc_Image.remove_object(rgb, tolerance = 5, energy = 'sobel', alg = 'dyn') Removes selected object from image. Object is selected by painting it with a given rgb value as demostrated in sunset_to_remove.jpg and dolphin_to_remove.jpg. *rgb(tuple): what color paint to be removed. *tolerance(int): the range (+/-) of colors around the given rgb to be removed. A high tolerance means that the detector will ensure that all of the selected object is removed at the expense of potential false positives. *energy (string): '...' *alg (string): '...'

Once the image has been resized, it can be outputted back to an image file using -->sc_Image.to_jpeg(filepath) where filepath is the file location to save the new image.