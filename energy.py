from math import fabs
#gets energy using e1 algorithm. helper methods may be added later
def Kroon_e1(pixel, neighbors):
        x, y = pixel.pos
        [n1, n2, n3, n4, px, n5, n6, n7, n8] = neighbors
        """
        | n1 n2 n3 |
        | n4 px n5 |
        | n6 n7 n8 |
        """
        pos_dx =  61 * n4.gray + 17 * n1.gray + 17 * n6.gray
        neg_dx =  - 61 * n5.gray - 17 * n3.gray - 17 * n8.gray
        dx = pos_dx + neg_dx

        pos_dy =  61 * n7.gray + 17 * n8.gray + 17 * n6.gray
        neg_dy = - 61 * n2.gray - 17 * n3.gray - 17 * n1.gray
        dy = pos_dy + neg_dy

        pixel.energy = fabs(dx) + fabs(dy)

        pixel.recalculate = False

        return pixel

def Sobel_e1(pixel, neighbors):
        x, y = pixel.pos
        [n1, n2, n3, n4, px, n5, n6, n7, n8] = neighbors
        """
        | n1 n2 n3 |
        | n4 px n5 |
        | n6 n7 n8 |
        """
        pos_dx =  2 * n4.gray + n1.gray + n6.gray
        neg_dx =  - 2 * n5.gray - n3.gray - n8.gray
        dx = pos_dx + neg_dx

        pos_dy =  2 * n7.gray + n8.gray + n6.gray
        neg_dy = - 2 * n2.gray - n3.gray - n1.gray
        dy = pos_dy + neg_dy

        pixel.energy = fabs(dx) + fabs(dy)

        pixel.recalculate = False

        return pixel

#gets energy using entropy algorithm. helper methods may be added later
def entropy(pixel, square):
	raise NotImplementedError