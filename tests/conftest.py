
import os
import shutil
import tempfile

import pytest

from rmxnmf import app as rmxnmfapp
from rmxnmf import config

DATA_TMP_FOLDER = 'datatmp'


def make_datatmp():

    dir = tempfile.mkdtemp()
    config.DATA_FOLDER = dir

    return config.DATA_FOLDER


@pytest.fixture()
def client():
    """Simple flask client."""
    rmxnmfapp.app.config['TESTING'] = True
    path = make_datatmp()
    with rmxnmfapp.app.test_client() as client:
        yield client
    shutil.rmtree(path)


@pytest.fixture(scope='class')
def cls_client(request):
    """Simple flask client for unittest TestCase classes."""
    rmxnmfapp.app.config['TESTING'] = True
    with rmxnmfapp.app.test_client() as client:
        request.cls.client = client
