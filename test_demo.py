def test_a():
    print("Still only this should run")
    assert False

def test_b():
    print("Not this")
    assert 1

def test_c():
    assert "non-empty"

