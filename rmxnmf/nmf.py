
import numpy
from sklearn.decomposition import NMF

from . import files


class NMFSklearn(object):

    def __init__(self,
                 matrix: (numpy.matrix, numpy.ndarray) = None,
                 init=None,
                 solver: str = 'mu',
                 feats_number: int = 10,
                 max_iter: int = 200):

        self.matrix = matrix
        self.feats_number = feats_number
        self.max_iter = max_iter
        self.init = init
        self.solver = solver

    def factorize(self):
        model = NMF(
            n_components=self.feats_number,
            init=self.init,
            random_state=0,
            max_iter=self.max_iter,
            solver=self.solver
        )
        W = model.fit_transform(self.matrix)
        H = model.components_
        return W, H


def call_nmf(path, feats: int = 10):

    matrix_path = files.matrix(path)
    feats_path = files.features(path)
    weights_path = files.weights(path)

    try:
        mtrx = numpy.load(matrix_path)
    except IOError as _err:
        raise _err
    except ValueError as _err:
        raise _err
    inst = NMFSklearn(matrix=mtrx, feats_number=feats)
    # W = weights; H = features
    W, H = inst.factorize()
    numpy.save(weights_path, W)
    numpy.save(feats_path, H)

    return feats_path, weights_path

