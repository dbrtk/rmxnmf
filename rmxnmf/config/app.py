
import os

DATA_FOLDER = os.environ.get('DATA_FOLDER')

MATRIX_FILE_NAME = 'matrix.npy'
FEATURES_FILE_NAME = 'features.npy'
WEIGHTS_FILE_NAME = 'weights.npy'

TARGET_FEATURES = 'feat.npy'
TARGET_WEIGHTS = 'weights.npy'

REDIS_HOST_NAME = os.environ.get('REDIS_HOST_NAME')
