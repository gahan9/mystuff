#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Gahan Saraiya
GiT: https://github.com/gahan9
StackOverflow: https://stackoverflow.com/users/story/7664524

Implementation for euclidean distance for any two N-dimensional points
"""

def euclidean_distance(a, b):
    """
    param a: tuple of point a1, a2, a3,...
    param b: tuple of point b1, b2, b3,...
    return: 
        False : if points are not having equal dimension to calculate
        otherwise
        euclidean distance between point a and b in any dimension
    """
    if len(a) != len(b):
        return False
    if len(a) < 2:
        return False
    squared_euclidean_distance = 0
    for idx, val in enumerate(a):
        squared_euclidean_distance += (val - b[idx])**2
    return squared_euclidean_distance**0.5

def test(dimension=3):
    import random
    p = tuple(random.randint(1, 10) for i in range(dimension))
    q = tuple(random.randint(1, 10) for i in range(dimension))
    distance = euclidean_distance(p, q)
    print("-"*20)
    print("Point 1: {} \nPoint 2: {}\nEuclidian Distance: {}\n".format(p, q, distance))
    print("-"*20)

if __name__ == "__main__":
    TESTS_TO_RUN = 5
    for i in range(TESTS_TO_RUN):
        test()
