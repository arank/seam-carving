from energy import e1, entropy
from seams import Seam, seam_dijk, seam_dyn

import Image



#representation of an image for seam carving
class sc_Image:
    def __init__(self, dimensions, pixels): 
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.pixels = pixels


    
    @classmethod
    def from_filepath(cls, filepath):
        """ Given an image file turns into an sc_Image class.
        eventually replace the im.getpixels calls with an im.getdata for performance reasons
        """
        pixels = {}
        im = Image.open (filepath)
        width, height = im.size
        for h in range(height):
            for w in range(width):
                pixels[(w,h)] = Pixel( (w,h), im.getpixel((w,h)) )
        return cls ((width, height), pixels)

    @classmethod
    def from_filepath2 (cls, filepath):
        """ Given an image file turns into an sc_Image class.
        Replaced the im.getpixels calls with an im.getdata for performance reasons
        """
        pixels = {}
        im = Image.open (filepath)
        width, height = im.size
        data = im.getdata()
        for w in range (width):
            for h in range (height):
                pixels[(w,h)] = Pixel( (w,h), data[ h * width + w]  )

        return cls ((width, height), pixels)

    # get the neighbors of the pixel at pos for e1 function
    def get_neighbors (self, pos):
        raise NotImplementedError

    # gets the 9x9 square of pixels of the pixel at pos for entropy function
    def get_square (self, pos):
        raise NotImplementedError

    def get_pixel(self, pos):
        if pos in self.pixels:
            return self.pixels[pos]
        else:
            return None

    # sets the energies of each pixel using the specified algorithm
    def set_energies (self, algorithm) :

        #map the energy calculating function to the pixel objects
        if algorithm == 'e1':
            map (lambda p: e1 (p, self.get_neighbors(p) ), self.pixels.values ) 

        elif algorithm == 'entropy':
            map (lambda p: entropy (p,  self.get_square(p) ), self.pixels.values ) 

        else:
            raise Exception("%s is not one of the implemented algorithms" % algorithm)

    # If resize is vertical, then calls seam_for_start_vert on every 
    # pixel at the left edge of the image and finds the lowest.
    # If resize is horizontal, then calls seam_for_start_hor on every
    # pixel at the top edge of the image and finds the lowest.
    def get_next_seam (self, alg = 'dyn', orientation = 'vertical') :

        #get all of the starting pixels
        if orientation == 'horizontal' : 
            starting_row = map (self.get_pixel, [(0,h) for h in range(self.height)] )
        elif orientation == 'vertical' :
            starting_row = map (self.get_pixel, [(w,0) for w in range(self.width)] )
        else:
            raise Exception("Orientation must be vertical or horizontal" )

        #create a list of seam objects representing the lowest seam originating
        #from each starting pixel
        if alg == 'dijk': 
            seams = map (seam_dijk, self.pixels)
        elif alg == 'dyn' :
            seams = map (seam_dyn, self.pixels)
        else:
            raise Exception("%s is not one of the implemented algorithms" % algorithm)

        def get_smaller(a,b):
            if a<b : return a
            else: return b
        seam = reduce (get_smaller, seams)

        return seam

    #write a jpeg representation of this image to a file
    def to_jpeg (self, filepath):
        data = [(0,0, 0)] * (self.width * self.height)
        for w in range (self.width):
            for h in range(self.height):
                data[h*self.width + w] = self.pixels[(w,h)].rgb
        im = Image.new("RGB", (self.width, self.height))
        im.putdata(data)
        im.save(filepath, "JPEG")


    #removes a seam from the image
    def remove_seam (self, seam) :
        raise NotImplementedError

    #calculate the lowest energy seams then add duplicates of them to the picture
    def enlarge (self, orientation, new_pixels, energy = 'e1', seam = 'dyn'):
        raise NotImplementedError


    # shrinks a picture by continouslly removing the lowest energy seem
    def shrink (self, orientation, new_pixels, energy = 'e1', seam = 'dyn'):
        for i in range(new_pixels) :
            self.set_energies (energy)
            self.remove_seam (self.get_next_seam(seam, orientation))

class Pixel:
    def __init__(self, pos, rgb): 
        self.pos = pos
        self.rgb = rgb
        self.energy = -1

    # to string function
    def __str__(self):
        return "[%s - %s]" % (str(self.pos), str(self.rgb))






