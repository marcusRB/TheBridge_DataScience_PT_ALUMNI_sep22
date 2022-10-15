import math
import numpy as np

def compute_all_distance(x,y):

    def eucl_dist():
        r1 = math.sqrt(sum([(coord[0]-coord[1])**2 for coord in zip(x,y)]))
        print(r1)

    def manh_dist():
        print(sum([abs(coord[0] - coord[1]) for coord in zip(x,y)]))

    return (eucl_dist(), manh_dist())


vec1 = np.array([5, 6, 7, -3])
vec2 = np.array([10, 1, 8, -6])

compute_all_distance(vec1, vec2)