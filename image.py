from energy import entropy
from energy import Sobel_e1 as e1
from seams import Seam, seam_dijk, seam_dyn
from random import randrange

import Image


def to_grayscale (img):
    return img.convert("L")

def from_pil ( im):
    pixels = {}
    width, height = im.size
    data = im.getdata()
    for w in range (width):
        for h in range (height):
            pixels[(w,h)] = Pixel( (w,h), data[ h * width + w]  )
    return pixels, width, height

#representation of an image for seam carving
class sc_Image:
    def __init__(self, dimensions, pixels, PIL): 
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.pixels = pixels
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

        

    def get_neighbors_simple (self, pos, pixels):

        x, y = pos
        data = []
        for j in range(y+1, y-2, -1):
            for i in range(x-1,x+2):
                try:
                    data.append(pixels[(i,j)])
                except KeyError:
                    data.append(None)
        return data

    def recalculate_neighbors(self, pos):
        for p in self.get_neighbors_simple (pos, self.pixels):
            if p is not None:
                p.to_recalculate()


    # gets the 3x3square of pixels of the pixel at pos for e1 function
    def get_neighbors (self, pos, pixels):

        data = self.get_neighbors_simple(pos, pixels)

        edge_replace = {0 : [2,6,8], 1 : [7], 2 : [0,8,6],
        3 : [5], 5 : [3], 6 : [0,8,2],  7 : [1], 8 : [2,6,0]
        }


        for i in range(len(data)):
            if data[i] is None:
                for replace_with in edge_replace[i] : 
                    if data[replace_with] is not None:
                        data [i] = data [replace_with]
                        break

        return data

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
            if pixel.recalculate :
                return e1 (pixel, self.get_neighbors (pixel.pos,self.pixels) )
            else :
                return pixel

        def set_energy_entropy(pixel):
            raise NotImplementedError

        #print 'p127-0 is None ', ( self.pixels[(127,0)] is None)
        if algorithm == 'e1':
            map (set_energy_e1 ,self.pixels.values() ) 

        elif algorithm == 'entropy':
            map (set_energy_entropy ,self.pixels.values() ) 

        else:
            raise Exception("%s is not one of the implemented algorithms" % algorithm)



    # If resize is vertical, then calls seam_for_start_vert on every 
    # pixel at the left edge of the image and finds the lowest.
    # If resize is horizontal, then calls seam_for_start_hor on every
    # pixel at the top edge of the image and finds the lowest.
    def get_next_seam (self, alg , orientation ) :

        #get all of the starting pixels
        if orientation == 'horizontal' : 
            raise NotImplementedError
        elif orientation == 'vertical' :
            if alg == 'dijk' :
                return seam_dijk(self, orientation)
            else :
                return seam_dyn(self,orientation)
        else:
            raise Exception("Orientation must be vertical or horizontal" )
        return seam

    def top_vert_row (self) :
        return map (self.get_pixel, [(0,h) for h in range(self.height)] )

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

    def to_energy_pic (self, filepath):

        pixels, w,h = from_pil (to_grayscale(self.PIL))
        self.pixels = pixels
        self.set_energies('e1')

        data = [0] * (self.width * self.height)
        for w in range (self.width):
            for h in range(self.height):
                data[h*self.width + w] = self.pixels[(w,h)].energy
        im = Image.new("L", (self.width, self.height))
        im.putdata(data)
        im.save(filepath, "JPEG")


    def remove_seam_vert2 (self, alg):

        seam = self.get_next_seam(alg, 'vertical')

        #print "To be removed: ",seam

        to_remove = seam
        #to_remove = map ( lambda p:  p.pos , filter(None, seam))

        for h in range(self.height):
            decrement = False
            for w in range (self.width):
                if not decrement:
                    if (w,h) in to_remove:
                        decrement = True
                        self.recalculate_neighbors((w,h))

                else:
                    self.pixels[(w,h)].shift_pos(-1,0)
                    self.pixels[(w-1,h)] = self.pixels[(w,h)]


            del self.pixels[self.width-1, h]

        self.width -= 1

        return seam


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


    def insert_seam(pixels, seam):
        raise NotImplementedError

    def get_n_seams(n, orientation ) :
        seams = []
        for i in range(n):
            self.set_energies(energy)
            if orientation == 'vertical':
                seams.append(self.remove_seam_vert2(alg))
        return seams

    #calculate the lowest energy seams then add duplicates of them to the picture
    def enlarge (self, orientation, new_pixels, energy = 'e1', alg = 'dijk'):

        original_pixels = self.pixels

        seams = self.get_n_seams(new_pixels, orientation)
       



        for s in seams:
            insert_seam(original_pixels, s)



    # shrinks a picture by continouslly removing the lowest energy seem
    def shrink (self, to_remove, orientation = "vertical", energy = 'e1', alg = 'dijk'):

        for i in range(to_remove) :
            self.set_energies (energy)

            if orientation == 'vertical' :
                seam = self.remove_seam_vert2 (alg)

            print i



class Pixel:
    def __init__(self, pos, rgb): 
        self.pos = pos
        self.original_pos = pos
        self.rgb = rgb

        r, g, b = self.rgb
        self.gray =  r + 256 * g + (256^2) * b

        self.energy = 0

        self.recalculate = True

    def shift_pos(self, dx, dy):
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)

    def to_recalculate(self):
        self.recalculate = True

    # to string function
    def __str__(self):
        return "[%s , %s]" % (str(self.pos), str(self.energy))
