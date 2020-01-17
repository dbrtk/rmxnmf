"""
Flask app for handling NMF.
"""

import io
import os
import shutil
import zipfile

from flask import abort, Flask, jsonify, request, send_file

from . import config
from .files import make_folder, upload_check
from .nmf import call_nmf

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():

    return jsonify({'success': True})


@app.route('/features/<int:feats>', methods=["POST"])
def create_features(feats: int = 10):
    """
    Creates features for a given matrix and features number.
    It expects an attachment that is a ".npy" file containing an ndarray.
    :return:
    """
    path = make_folder()
    matrix_path = os.path.join(path, config.MATRIX_FILE_NAME)

    if 'file' not in request.files:
        return abort(404)
    file = request.files['file']
    file.save(matrix_path)

    if not upload_check(path=path):
        shutil.rmtree(path)
        return abort(403)

    feats_path, weights_path = call_nmf(path=path, feats=feats)

    mem_file = io.BytesIO()
    with zipfile.ZipFile(
            mem_file, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(feats_path, arcname=config.TARGET_FEATURES)
        zf.write(weights_path, arcname=config.TARGET_WEIGHTS)

    shutil.rmtree(path)
    mem_file.seek(0)
    return send_file(
        mem_file,
        as_attachment=True,
        attachment_filename='payload.zip',
        mimetype='application/zip'
    )




