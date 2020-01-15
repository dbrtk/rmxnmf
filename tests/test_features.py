
import io
import tempfile
import unittest

import numpy
import pytest


@pytest.mark.usefixtures('cls_client')
class Test(unittest.TestCase):

    def setUp(self) -> None:

        self.W = 1000
        self.H = 100
        self.arr = numpy.random.rand(self.W, self.H)
        self.feats = 10
        # byte_file = io.BytesIO()

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

    def test_resp_status_code(self):

        self.assertEqual(self.resp.status_code, 200)

