def manh_dist(x,y):
    return sum([abs(coord[0] - coord[1]) for coord in zip(x,y)])
