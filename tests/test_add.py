from myproj import add


def test_add_positive():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -1) == -2
