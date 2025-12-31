import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(10, 5) == 5
    assert calculator.sub(0, 5) == -5
