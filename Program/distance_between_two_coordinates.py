# Write a program to find the euclidean distance between two coordinates.

import math

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two coordinates."""
    distance = math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)
    return distance

# Example coordinates
coord1 = (3, 4)
coord2 = (6, 8)

distance = euclidean_distance(coord1, coord2)
print("Euclidean distance between", coord1, "and", coord2, "is:", distance)
