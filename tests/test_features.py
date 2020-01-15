
import io
import os
import shutil
import tempfile
import unittest
import zipfile

import numpy
import pytest

from rmxnmf import config


@pytest.mark.usefixtures('cls_client')
class Test(unittest.TestCase):

    def setUp(self) -> None:

        self.W = 1000
        self.H = 100
        self.arr = numpy.random.rand(self.W, self.H)
        self.feats = 10

        _file = tempfile.TemporaryFile()
        numpy.save(_file, self.arr)
        _file.seek(0)

        self.resp = self.client.post(
            f'/features/{self.feats}',
            data={
                'file': (_file, 'matrix.npy')
            },
            content_type='multipart/form-data',
        )
        _file = io.BytesIO()
        _file.write(self.resp.get_data())
        zf = zipfile.ZipFile(_file, "a", zipfile.ZIP_DEFLATED, False)

        tmpdir = tempfile.TemporaryDirectory()
        zf.extractall(tmpdir.name)
        self.features = numpy.load(
            os.path.join(tmpdir.name, config.TARGET_FEATURES))
        self.weights = numpy.load(
            os.path.join(tmpdir.name, config.TARGET_WEIGHTS))
        shutil.rmtree(tmpdir.name)

    def test_resp_status_code(self):

        self.assertEqual(self.resp.status_code, 200)

    def test_resp_mimetype(self):

        self.assertEqual(self.resp.mimetype, 'application/zip')

    def test_file(self):

        self.assertIsInstance(self.resp.get_data(), bytes)

    def test_features_type(self):

        self.assertIsInstance(self.features, numpy.ndarray)

    def test_weights_type(self):

        self.assertIsInstance(self.weights, numpy.ndarray)

    def test_features_shape(self):

        self.assertEqual(
            self.features.shape,
            (self.W, self.feats)
        )

    def test_weights_shape(self):

        self.assertEqual(
            self.weights.shape,
            (self.feats, self.H)
        )

