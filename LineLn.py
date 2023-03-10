import math


def line_length(dot1, dot2):
    x = dot2[0] - dot1[0]
    y = dot2[1] - dot1[1]
    hyp = math.sqrt(x ** 2 + y ** 2)
    return round(hyp, 2)

