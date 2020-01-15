
import unittest

import numpy

from rmxnmf.nmf import NMFSklearn


class TestNMF(unittest.TestCase):

    def setUp(self) -> None:

        self.w_shape = 1000
        self.h_shape = 100
        self.feats = 10

        self.arr = numpy.random.rand(self.w_shape, self.h_shape)
        self.inst = NMFSklearn(matrix=self.arr, feats_number=self.feats)
        W, H = self.inst.factorize()

        self.features = W
        self.weights = H

    def test_feats_type(self):
        self.assertIsInstance(self.features, numpy.ndarray)

    def test_weights_type(self):
        self.assertIsInstance(self.weights, numpy.ndarray)

    def test_shape_feats(self):
        self.assertEqual(
            self.features.shape,
            (self.w_shape, self.feats)
        )

    def test_shape_weights(self):
        self.assertEqual(
            self.weights.shape,
            (self.feats, self.h_shape)
        )
