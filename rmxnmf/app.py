"""
Flask app that handles http requests and sends files back to the client.
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

    feats_path, weights_path = call_nmf(path=path, **request.args)

    mem_file = io.BytesIO()
    with zipfile.ZipFile(
            mem_file, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(feats_path)
        zf.write(weights_path)

    shutil.rmtree(path)

    return send_file(mem_file,
                     attachment_filename='payload.zip',
                     mimetype='application/zip')




