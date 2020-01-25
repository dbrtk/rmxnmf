
import os

from .app import celery
from .config.app import TARGET_FEATURES, TARGET_WEIGHTS
from .nmf import call_nmf


@celery.task
def factorize_matrix(
        matrix_path: str = None,
        target_path: str = None,
        feats_file_name: str = TARGET_FEATURES,
        weights_file_name: str = TARGET_WEIGHTS,
        feature_number: int = 10) -> (str, int, str, str, str):
    """
    :param matrix_path:
    :param target_path:
    :param feats_file_name:
    :param weights_file_name:
    :param feature_number:
    :return:
    """
    feats_path, weights_path = call_nmf(
        matrix_path=matrix_path,
        feats=feature_number,
        feats_path=os.path.join(target_path, feats_file_name),
        weights_path=os.path.join(target_path, weights_file_name)
    )
    if not os.path.exists(feats_path):
        raise RuntimeError(feats_path)
    if not os.path.exists(weights_path):
        raise RuntimeError(weights_path)

