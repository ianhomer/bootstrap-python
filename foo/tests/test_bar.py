from .. import Bar


def test_bar():
    assert Bar().ok


def test_sum():
    assert Bar().sum(1, 2) == 3
