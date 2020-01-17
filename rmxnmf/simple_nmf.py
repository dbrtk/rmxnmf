

import numpy
import random


def difcost(a, b):
    dif = 0
    # Loop over every row and column in the matrix
    for i in range(numpy.shape(a)[0]):
        for j in range(numpy.shape(a)[1]):
            # Add together the differences
            dif += pow(a[i, j] - b[i, j], 2)
    return dif


def factorize(v, pc=10, iter=50):
    """
    """
    ic = numpy.shape(v)[0]
    fc = numpy.shape(v)[1]

    # Initialize the weight and feature matrices with random values
    # Weight Matrix
    w = numpy.ndarray([[random.random() for j in range(pc)] for i in range(ic)])

    # Feature Matrix
    h = numpy.ndarray([[random.random() for i in range(fc)] for i in range(pc)])

    # Perform operation a maximum of iter times
    for i in range(iter):
        wh = w * h

        # Calculate the current difference
        cost = difcost(v, wh)

        if i % 10 == 0:
            pass
            # print(cost)
        # Terminate if the matrix has been fully factorized
        if cost == 0:
            break

        # Update feature matrix
        hn = (numpy.transpose(w) * v)
        hd = (numpy.transpose(w) * w * h)
        h = numpy.ndarray(numpy.array(h) * numpy.array(hn) / numpy.array(hd))
        # Update weights matrix
        wn = (v * numpy.transpose(h))
        wd = (w * h * numpy.transpose(h))

        w = numpy.ndarray(numpy.array(w) * numpy.array(wn) / numpy.array(wd))

        if numpy.any(numpy.isnan(w)):
            w = numpy.nan_to_num(w)

    # returns (weights, features)
    return w, h


if __name__ == '__main__':

    m1 = numpy.ndarray([[1, 2, 3], [4, 5, 6]])
    m2 = numpy.ndarray([[1, 2], [3, 4], [5, 6]])

    # print(m1)
    # print(m2)

    w, h = factorize(m1 * m2, pc=3, iter=100)

    # print(w)
    # print(h)
