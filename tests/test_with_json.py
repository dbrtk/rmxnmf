
import json
import numpy
import tempfile


def test_with_json():

    arr_a = numpy.random.rand(100, 100)
    val = json.dumps({'data': arr_a.tolist()})
    assert isinstance(val, str)
    val = json.loads(val)
    assert numpy.array_equal(arr_a, val.get('data'))


def test_with_memfile():

    arr_a = numpy.random.rand(1000, 100)
    _file = tempfile.TemporaryFile()
    numpy.save(_file, arr_a)
    _file.seek(0)
    arr_b = numpy.load(_file)
    assert numpy.array_equal(arr_a, arr_b)



