from energy import entropy
from energy import Sobel_op as e1
from energy import Sobel_five_op as e1_five
from seams import Seam, seam_dijk, seam_dyn
from random import randrange

import copy
import Image

# Grayscales the image so that we can run energy calculations on it
def to_grayscale (img):
    return img.convert("L")
# creates image sc object from python image library representation of a picture
def from_pil (im):
    this_id = 0
    pixels = {}
    width, height = im.size
    data = im.getdata()
    for w in range (width):
        for h in range (height):

            color = data[ h * width + w]
            #we are working with a color image for the normal picture and have an rgb tuple
            if isinstance (color, tuple) :
                pixels[(w,h)] = Pixel( (w,h), color  )
                this_id += 1

            #we are working with a grayscale image for the energy picture and an int
            elif isinstance (color, int) :
                pixels[(w,h)] = Pixel( (w,h), (0,0,0), gray = color  )
    return pixels, width, height

# representation of an image for seam carving with all the methods encapsulating critical
# functions to seam generation
class sc_Image:
    def __init__(self, dimensions, pixels, PIL): 
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.pixels = pixels
        self.dim = 3
        self.PIL = PIL
    

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
        return cls ((width, height), pixels, im)       
    
    @classmethod
    def from_filepath2 (cls, filepath):
        """ Given an image file turns into an sc_Image class.
        Replaced the im.getpixels calls with an im.getdata for performance reasons
        """

        im = Image.open (filepath)
        pixels, width, height = from_pil(im)
        return cls ((width, height), pixels, im)

    # gets neigbors to pixel at given position in image in form of pixle list
    def get_neighbors_simple (self, pos, pixels, dim):
        x, y = pos
        data = []
        for j in range(y+(dim/2), y-(dim/2+1), -1):
            for i in range(x-(dim/2),x+(dim/2+1)):
                try:
                    data.append(pixels[(i,j)])
                except KeyError:
                    data.append(None)
        return data

    # flags neigboring pixles to pixle being removed so they can be recalculated by energy algorithm 
    def recalculate_neighbors(self, pos, dim):
        for p in self.get_neighbors_simple (pos, self.pixels, self.dim):
            if p is not None:
                p.to_recalculate()


    # gets the dim x dim square of pixels of the pixel at pos for energy functions
    def get_neighbors (self, pos, pixels, dim):

        data = self.get_neighbors_simple(pos, pixels, dim)

        if (dim == 3):
            edge_replace = {0 : [2,6,8], 1 : [7], 2 : [0,8,6],
            3 : [5], 5 : [3], 6 : [0,8,2],  7 : [1], 8 : [2,6,0]}
        
            for i in range(len(data)):
                if data[i] is None:
                    for replace_with in edge_replace[i] : 
                        if data[replace_with] is not None:
                            data [i] = data [replace_with]
                            break

        return data

    # get neighbors within a 5X5 square of the target pixel retrurning a list of pixles
    def get_five_neighbors (self, pos, pixels) :

        x, y = pos
        data = []
        for j in range(y+2, y-3, -1):
            for i in range(x-2,x+3):
                data.append(pixels[(i,j)])
        return data


    # gets pixle object at given postion
    def get_pixel(self, pos):
        if pos in self.pixels:
            return self.pixels[pos]
        else:
            return None


    # sets the energies of each pixel using the specified algorithm
    def set_energies (self, algorithm) :
        #map the energy calculating function to the pixel objects

        #print self.pixels[(127,107)

        def set_energy_e1 (pixel):
            self.dim = 3
            if pixel.recalculate :
                return e1 (pixel, self.get_neighbors (pixel.pos,self.pixels,self.dim) )
            else :
                return pixel

        def set_energy_e1_five (pixel) :
            self.dim = 5
            if pixel.recalculate :
                return e1_five (pixel, self.get_five_neighbors (pixel.pos,temp_pix) )
            else :
                return pixel

        def set_energy_entropy(pixel):
            self.dim = 9
            if pixel.recalculate :
                return entropy (pixel, self.get_neighbors (pixel.pos,self.pixels,self.dim) )
            else :
                return pixel

        #print 'p127-0 is None ', ( self.pixels[(127,0)] is None)
        if algorithm == 'e1':
            map (set_energy_e1 ,self.pixels.values() ) 

        elif algorithm == 'e1_five':
            temp_pix = self.pixels

            for h in [-2, -1, self.height, self.height +1] : 
                for w in range(self.width):
                    if h == -1 or h == -2:
                        temp_pix[(w,h)] = Pixel( (w,h), self.pixels[(w, 0)].rgb )
                    else:
                        temp_pix[(w,h)] = Pixel( (w,h), self.pixels[(w, self.height -1)].rgb )

            for w in [-2, -1, self.width, self.width +1]:
                for h in range(-2, self.height + 2):
                    if w == -1 or w == -2:
                        if h == -1 or -2:
                            temp_pix[(w,h)] = Pixel( (w,h), self.pixels[(0,0)].rgb )
                        elif h == self.height or h == self.height + 1:
                            temp_pix[(w,h)] = Pixel( (w,h), self.pixels[(0,self.height-1)].rgb )
                        else:
                            temp_pix[(w,h)] = Pixel((w,h), self.pixels[(0, h)].rgb )
                    else:
                        if h == -1 or -2:
                            temp_pix[(w,h)] = Pixel( (w,h), self.pixels[(self.width-1,0)].rgb )
                        elif h == self.height or h == self.height + 1:
                            temp_pix[(w,h)] = Pixel( (w,h), self.pixels[(self.width-1,self.height-1)].rgb)
                        else:
                            temp_pix[(w,h)] = Pixel((w,h), self.pixels[(self.width-1, h)].rgb )

            for h in range(self.height):
                for w in range(self.width):
                    set_energy_e1_five( temp_pix[(w,h)] )

        elif algorithm == 'entropy':
            map (set_energy_entropy ,self.pixels.values() ) 

        else:
            raise Exception("%s is not one of the implemented algorithms" % algorithm)



    # If resize is vertical, then calls seam_for_start_vert on every 
    # pixel at the left edge of the image and finds the lowest.
    # If resize is horizontal, then calls seam_for_start_hor on every
    # pixel at the top edge of the image and finds the lowest.
    def get_next_seam (self, alg ) :

        #get all of the starting pixel
        if alg == 'dijk' :
            return seam_dijk(self)
        else :
            return seam_dyn(self)
        return seam
    
    # gets the leftmost verical row in ordered list
    def top_vert_row (self) :
        return map (self.get_pixel, [(0,h) for h in range(self.height)] )

    # gets the top horizonal row of pixles in ordered list
    def top_horz_row (self) :
        return map (self.get_pixel, [(w,0) for w in range(self.width)] )

    #write a jpeg representation of this image to a file
    def to_jpeg (self, filepath):
        data = [(0,0, 0)] * (self.width * self.height)
        for w in range (self.width):
            for h in range(self.height):
                # print "(%s, %s); (%s, %s)" % (w,h, self.width, self.height)
                data[h*self.width + w] = self.pixels[(w,h)].rgb
        im = Image.new("RGB", (self.width, self.height))
        im.putdata(data)
        im.save(filepath, "JPEG")

    #Uses the grayscale of the image to get an energy map
    def to_energy_pic (self, filepath, energy = 'e1'):
        original_pixels = self.pixels
        gray_pixels, w, h = from_pil (to_grayscale(self.PIL))
        self.pixels = gray_pixels
        self.set_energies(energy)

        data = [0] * (self.width * self.height)
        for w in range (self.width):
            for h in range(self.height):
                data[h*self.width + w] = self.pixels[(w,h)].energy
        im = Image.new("L", (self.width, self.height))
        im.putdata(data)
        im.save(filepath, "JPEG")

        self.pixels = original_pixels

    # removes a vertical seam
    def remove_seam_vert2 (self, alg, return_pixels = False):

        seam = self.get_next_seam(alg)

        #print "To be removed: ",seam

        to_remove = seam

        # copy all pixels to return later if needed
        if return_pixels:
            pixels = map( lambda p : copy.deepcopy (self.get_pixel(p)), seam)
        else:
            pixels = []

        #to_remove = map ( lambda p:  p.pos , filter(None, seam))

        for h in range(self.height):
            decrement = False
            for w in range (self.width):
                if not decrement:
                    if (w,h) in to_remove:
                        decrement = True
                        self.recalculate_neighbors((w,h), self.dim)

                else:
                    self.pixels[(w,h)].shift_pos(-1,0)
                    self.pixels[(w-1,h)] = self.pixels[(w,h)]

            del self.pixels[self.width-1, h]

        self.width -= 1

        return pixels


    #debugging function that makes sure self.pixels is consistent
    def check_for_mismatch(self):
        for h in range(self.height): 
            for w in range (self.width): 
                if self.pixels[(w,h)].pos != (w,h) :
                    print 'mismatch at ', w, h, "-- ",self.pixels[(w,h)].pos

    #debugging function that checks self.pixels for None types
    def check_for_none(self):
        for h in range(self.height): 
            for w in range (self.width):
                if self.pixels[(w,h)] is None:
                    print "(%s, %s) is None" % (w,h)

    # copies back in a remembered seam for enlargement
    def insert_seam(self,pixels, seam):

        for pixel in seam:

            h = pixel.pos[1]

            for w in range (self.width-1, -1, -1):


                if pixel.original_pos == (w,h):
                
                    pixel.pos = (w+1,h)
                    pixels[(w+1,h)] = pixel
                    
                    #update rgb value
                    left = pixels[(w,h)].rgb

                    if (w+2,h) in pixels:
                        right = pixels[(w+2,h)].rgb

                    else :
                        right  = pixel.rgb
                    pixel.rgb = self.average_rbg(left, right)
                    
                    break

                else :
                    pixels[(w,h)].shift_pos(1,0)
                    pixels[(w+1,h)] = pixels[(w,h)]




        self.width += 1
        return pixels

    # averages the coler of two rgbs from pixles
    def average_rbg(self, rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2

        return ((r1+r2)/2, (g1+g2)/2, (b1+b2)/2)
    
    # grabs first n seams found in image
    def get_n_seams(self,n, energy, alg) :


        seams = []
        for i in range(n):
            self.set_energies(energy)
            seam = self.remove_seam_vert2(alg, return_pixels = True)
            seams.append( seam )

            print "Got %d seams" % (i+1)

        return seams

    #calculate the lowest energy seams then add duplicates of them to the picture
    def enlarge (self,  new_pixels, orientation = 'vertical', energy = 'e1', alg = 'dyn'):

        if orientation == 'horizontal' :
            self.transpose()


        original_pixels = copy.deepcopy(self.pixels)

        original_width =self.width
        original_height = self.height

        seams = self.get_n_seams(new_pixels, energy, alg)


        self.width = original_width
        self.height = original_height

       
        for s in seams:
            self.insert_seam(original_pixels, s)


        self.pixels = original_pixels

        if orientation == 'horizontal' :
            self.transpose()



    # shrinks a picture by continouslly removing the lowest energy seem
    def shrink (self, to_remove, orientation = "vertical", energy = 'e1', alg = 'dyn'):

        counter = 0

        #if we are taking horizontal seams transpose the image first
        if orientation == 'horizontal' :
            self.transpose()

        for i in range(to_remove) :
            counter += 1
            self.set_energies (energy)

            seam = self.remove_seam_vert2 (alg)

            print "Removed %d seams" % (counter)

        if orientation == 'horizontal' :
            self.transpose()    


    # transposes the image so we can operate on it vertically and horizonatally. It re instatiates object ivars
    def transpose (self) :
        new_pix = {}
        for i in range(self.width):
            for j in range(self.height):
                new_pix[(j,i)]= Pixel( (j,i), self.pixels[(i,j)].rgb )
        self.pixels = new_pix
        tmp = self.height
        self.height = self.width
        self.width = tmp

# Class that encapsulates pixle data in image sc object including the energy, the unique identifier, the color the postion
# and a suite of methods to interact with it in the context of the image object
class Pixel:
    def __init__(self, pos, rgb, gray = None): 
        self.pos = pos
        self.original_pos = pos
        self.rgb = rgb

        #if gray wasn't explicitly set initialize it based off color
        if gray is None:
            r, g, b = self.rgb
            self.gray =  r + 256 * g + (256^2) * b
        else:
            self.gray = gray



        self.energy = 0

        self.recalculate = True

    # shifts pixle position by updating ivar
    def shift_pos(self, dx, dy):
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)

    # mark to see if it needs to be re energized
    def to_recalculate(self):
        self.recalculate = True

    # to string function
    def __str__(self):
        return "[%s , %s]" % (str(self.pos), str(self.energy))
