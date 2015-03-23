from pybaldr import *

def test_read_baldr_file():
    
    with open('tests/data/example.baldr', 'rb') as f:
        results = full_read(f.read())
    assert isinstance(results, list)
    assert isinstance(results[0], BaldrRecord)
    assert len(results[0]) == 1
    assert results[0].body == "9"
    assert len(results) > 100
    assert int(results[100].body) > 10000000
    for r in results:
        int(r.body) # All the examples are ints
    assert True # completed