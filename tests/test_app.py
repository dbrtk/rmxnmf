
import json


def test_home_page(client):

    resp = client.get('/')
    resp = json.loads(resp.get_data())
    assert isinstance(resp, dict)
    assert resp.get('success') is True


