import numpy

import matrices


class Style:
    def next(self, grid):
        return numpy.matrix(
                numpy.apply_along_axis(lookup, 2, matrices.windows(grid)))


def grow(matrix):
    grown_v = numpy.concatenate((matrix[-1, :], matrix, matrix[0, :]), axis=0)
    grown = numpy.concatenate((grown_v[:, -1], grown_v, grown_v[:, 0]), axis=1)
    return grown


def lookup(array):
    return 1 if matrices.integer_repr(array) in alive else 0


alive = set(map(matrices.integer_repr, [
    [0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0],

    [0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0],

    [0, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 0],
]))
