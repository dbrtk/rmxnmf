
from io import StringIO

from flask import abort, Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():

    return jsonify()


@app.route('/features/<objectid:containerid>/<int:feats>', methods=["POST"])
def create_features(containerid: str = None, feats: int = 10):
    """
    Creates features for a given container id and feats number.
    :return:
    """
    # access parameters encoded in the url
    request.args.get('')

    if 'file' not in request.FILES:
        return abort(500)


    pass



