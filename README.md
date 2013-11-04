seam-carving
+AD0APQA9AD0APQA9AD0APQA9AD0APQA9-

Seam Carving (CS51 Project)

By: Aran Khanna, Andrew Mauboussin, Sergei Balanovich

Dependency: Python Imaging Library (PIL)

A Python library to perform content-aware image resizing methods like image scaling and object removal using seam carving. Check out the images folder for some examples.  


To run: Edit main.py to specify the seam carving operations to be performed. Example code is provided in the file and test images are in the data folder. Then execute main.py (+ACI-python main.py+ACI- in a unix shell). 


Our project is implemented in the form of a class, sc+AF8-Image (seam-carving image).

To use our seam carving methods on image, the first step is creating an sc+AF8-Image object. The constructor for sc+AF8-Image takes the filepath of a an image file. Here is an example of how to create an sc+AF8-Image object: 

--+AD4-im +AD0- image.sc+AF8-Image.from+AF8-filepath(+ACI-comet.jpg+ACI-)


Once an sc+AF8-Image has been created, we have some public methods to use to resize the image using 
seam carving:

--+AD4-sc+AF8-Image.shrink(to+AF8-remove, orientation +AD0- +ACI-vertical+ACI-, energy +AD0- 'e1', alg +AD0- 'dijk')
Shrinks an image in one direction.
+ACo-to+AF8-remove (int): the number of pixels to be removed from the image.
+ACo-orientation (string): the direction the seams run in. The two options are 'vertical' and 'horizontal'. Vertical will alter the image's width and horizontal will change its height.
+ACo-energy (string): the energy function to be applied to the image. The options are 'sobel' 'scharr' 'kroon' 'sobel5' 'scharr5' and 'entropy'. The first three use 3x3 pixel filters with varying weights. The next two use 5x5 pixel filters. The final one uses a 9x9 histogram to calculate the entropy of a every pixel. Be aware that the first three will run more quickly than the others.
+ACo-alg (string): the shortest path algorithm to be used. The two options are 'dijk' and 'dyn'. Be aware that dijkstra's doesn't work with enlarge or remove object due to the way it deals with negative energy values.

--+AD4-sc+AF8-Image.enlarge(new+AF8-pixels, orientation +AD0- 'vertical', energy +AD0- '', alg +AD0- 'dyn')
Enlarges an image in one direction.
+ACo-new+AF8-pixels (int): the number of pixels to be added to the image.
+ACo-orientation (string): Same options and functionality as shrink.
+ACo-energy (string): '...'
+ACo-alg (string): '...'

--+AD4-sc+AF8-Image.enlarge+AF8-object+AF8-1d(new+AF8-pixels, orientation+AD0AIg-vertical+ACI-, energy+AD0-'sobel', alg+AD0-'dyn')
Enlarges high-energy objects in one dimension while retaining the size of the original photo.
+ACo-new+AF8-pixels (int): the number of pixels by which high energy objects should be enlarged.
+ACo-orientation (string): '...'
+ACo-energy (string): '...'
+ACo-alg (string): '...'

--+AD4-sc+AF8-Image.enlarge+AF8-object(seams, energy +AD0- 'sobel', alg +AD0- 'dyn')
Enlarges high-energy objects in two dimensions.
+ACo-seams (int): the number of seams by which high energy objects should be enlarged
+ACo-energy (string): '...'
+ACo-alg (string)+ADs- '...'

--+AD4-sc+AF8-Image.remove+AF8-object(rgb, tolerance +AD0- 5, energy +AD0- 'sobel', alg +AD0- 'dyn')
Removes selected object from image. Object is selected by painting it with a given rgb value as demostrated in sunset+AF8-to+AF8-remove.jpg and dolphin+AF8-to+AF8-remove.jpg.
+ACo-rgb(tuple): what color paint to be removed.
+ACo-tolerance(int): the range () of colors around the given rgb to be removed. A high tolerance means that the detector will ensure that all of the selected object is removed at the expense of potential false positives.
+ACo-energy (string): '...'
+ACo-alg (string): '...'

Once the image has been resized, it can be outputted back to an image file using
--+AD4-sc+AF8-Image.to+AF8-jpeg(filepath) where filepath is the file location to save the new image.
