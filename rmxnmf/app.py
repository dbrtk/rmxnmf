
from io import StringIO

from flask import abort, Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():

    return jsonify()


@app.route('/features/<objectid:containerid>', methods=["GET"])
def available_features(containerid: str = None):
    """
    Retrieves available features for a container.
    :return:
    """
    pass


@app.route('/features/<objectid:containerid>/<int:feats>', methods=["POST"])
def create_features(containerid: str = None, feats: int = 10):
    """
    Creates features for a given container id and feats number.
    :return:
    """
    # access parameters encoded in the url
    request.args.get('')
    pass


@app.route('/features/<objectid:containerid>/<int:feats>', methods=["GET"])
def get_features(containerid: str = None, feats: int = None):
    """
    Retrieves features for a given container id and a given features number.
    :return:
    """

    pass


@app.route('/features/<objectid:containerid>/<int:feats>', methods=["DELETE"])
def del_features(containerid: str = None, feats: int = None):
    """
    Deletes features for a given container id and features number.
    :return:
    """

    pass


