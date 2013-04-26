from math import fabs
#gets energy using e1 algorithm. helper methods may be added later
def e1(pixel, neighbors):
        x, y = pixel.pos
        [n1, n2, n3, n4, px, n5, n6, n7, n8] = neighbors
        """
        | n1 n2 n3 |
        | n4 px n5 |
        | n6 n7 n8 |
        """
        pos_dx = 4 * pixel.rgb - 2 * n4.rgb - n1.rgb - n6.rgb
        neg_dx = 4 * pixel.rgb - 2 * n5.rgb - n3.rgb - n8.rgb
        dx = pos_dx - neg_dx

        pos_dy = 4 * pixel.rgb - 2 * n7.rgb - n8.rgb - n6.rgb
        neg_dy = 4 * pixel.rgb - 2 * n2.rgb - n3.rgb - n1.rgb
        dy = pos_dy - neg_dy

        pixel.energy = fabs(dx) + fabs(dy)
        
        return pixel

#gets energy using entropy algorithm. helper methods may be added later
def entropy(pixel, square):
	raise NotImplementedError