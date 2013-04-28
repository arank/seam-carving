from math import fabs, log
#gets energy using e1 algorithm. helper methods may be added later

def three_three_filter(pixel, neighbors, a, b):
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

def five_five_filter(pixel, n, a, b, c, d, e, f):
    pos_dx = a*n[11].gray + b*n[10].gray + c*(n[6].gray + n[16].gray) + d*(n[5].gray + n[15].gray) + e*(n[1].gray + n[21].gray) + f*(n[0].gray+n[20].gray)
    neg_dx = a*n[13].gray + b*n[14].gray + c*(n[8].gray + n[18].gray) + d*(n[9].gray + n[8].gray) + e*(n[3].gray + n[23].gray) + f*(n[4].gray + n[24].gray)
    dx = pos_dx - neg_dx
    pos_dy = a*n[17].gray + b*n[22].gray + c*(n[16].gray + n[18].gray) + d*(n[21].gray + n[23].gray) + e*(n[15].gray + n[19].gray) + f*(n[20].gray+n[24].gray)
    neg_dy = a*n[7].gray + b*n[2].gray + c*(n[6].gray + n[8].gray) + d*(n[1].gray + n[3].gray) + e*(n[5].gray + n[9].gray) + f*(n[0].gray + n[4].gray)
    dy = pos_dy - neg_dy

    pixel.energy = fabs(dx) + fabs(dy)

    pixel.recalculate = False

    return pixel

def Sobel_five_op(pixel, neighbors):
    return five_five_filter(pixel, neighbors, 20, 10, 10, 8, 4, 5)

def Scharr_five_op(pixel, neighbors):
    return five_five_filter(pixel, neighbors, 6, 3, 2, 2, 1, 1)

#gets energy using entropy algorithm. helper methods may be added later
#Code still buggy, but getting there. Will be implemented along with
#image expansion for the final submission
##def entropy(pixel, square):
##    num_bins = 10
##    pix_range = 16844000
##    b = pix_range/num_bins
##    hist_len = len(square)
##    dim = hist_len**(.5)
##    histogram = {b:1, 2*b:1, 3*b:1, 4*b:1, 5*b:1, 6*b:1, 7*b:1, 8*b:1, 9*b:1, 10*b:1}
##    for x in range (hist_len):
##        for k, v in histogram.iteritems():
##            if square[x] < k:
##                histogram[k] += 1
##                print histogram[k]
##    square_prob = [float(v)/hist_len for k, v in histogram.iteritems()]
##
##    #Shannon entropy formula with a base 2 log. Source:
##    #http://upload.wikimedia.org/math/8/7/e/87efdf0d38947240683250d3a24466e0.png
##    pixel.energy = -sum([p*(log(p, 2)) for p in square_prob])
##    pixel.recalculate = False
##    return pixel
##
