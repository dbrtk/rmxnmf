"""Handling files."""

import os
import uuid

import numpy

from . import config


def make_folder(unique_id: str = None):

    path = os.path.join(
        config.DATA_FOLDER, unique_id if unique_id else uuid.uuid4().hex)
    os.mkdir(path)
    return path


def matrix(path): return os.path.join(path, config.MATRIX_FILE_NAME)


def features(path): return os.path.join(path, config.FEATURES_FILE_NAME)


def weights(path): return os.path.join(path, config.WEIGHTS_FILE_NAME)


def upload_check(path):

    try:
        arr = numpy.load(matrix(path))
    except (IOError, ValueError) as _err:
        return False
    if isinstance(arr, (numpy.ndarray, numpy.matrix)):
        return True
    return False
