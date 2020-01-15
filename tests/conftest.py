

import pytest

from rmxnmf import app as rmxnmfapp


@pytest.fixture(scope='session')
def client():
    """Simple flask client."""
    rmxnmfapp.app.config['TESTING'] = True
    with rmxnmfapp.app.test_client() as client:
        yield client


@pytest.fixture(scope='class')
def cls_client(request):
    """Simple flask client for unittest TestCase classes."""
    rmxnmfapp.app.config['TESTING'] = True
    with rmxnmfapp.app.test_client() as client:
        request.cls.client = client

