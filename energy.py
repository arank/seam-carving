from math import fabs
#gets energy using e1 algorithm. helper methods may be added later


def three_three_filter(pixel, neighbors, a, b):
        x, y = pixel.pos
        [n1, n2, n3, n4, px, n5, n6, n7, n8] = neighbors
        """
        | n1 n2 n3 |
        | n4 px n5 |
        | n6 n7 n8 |
        """
        pos_dx =  a * n4.gray + b * n1.gray + b * n6.gray
        neg_dx =  - a * n5.gray - b * n3.gray - b * n8.gray
        dx = pos_dx + neg_dx

        pos_dy =  a * n7.gray + b * n8.gray + b * n6.gray
        neg_dy = - a * n2.gray - b * n3.gray - b * n1.gray
        dy = pos_dy + neg_dy

        pixel.energy = fabs(dx) + fabs(dy)

        pixel.recalculate = False

        return pixel

def Kroon_op(pixel, neighbors):
        return three_three_filter(pixel, neighbors, 61, 17)

def Scharr_op(pixel, neighbors):
        return three_three_filter(pixel, neighbors, 10, 3)

def Sobel_op(pixel, neighbors):
        return three_three_filter(pixel, neighbors, 2, 1)

#gets energy using entropy algorithm. helper methods may be added later
def entropy(pixel, square):
	raise NotImplementedError