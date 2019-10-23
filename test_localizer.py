from localizer import find_ground
import math

TOLERANCE = 0.5


def test_timeout():
    assert find_ground(10000000, 0, 0, 0, 0) is None

    assert find_ground(10, 0, 0, math.pi / 2, 0) is None

    assert find_ground(10, 0, 0, 0, math.pi / 2) is None


def test_simple():
    assert find_ground(0, 0, 0, 0, 0) == (0, 0)

    assert find_ground(0, 10, 10, 0, 0) == (10, 10)

    n, e = find_ground(10, 0, 0, 0, math.asin(5 / math.sqrt(125)))
    assert math.isclose(0, n, rel_tol=TOLERANCE)
    assert math.isclose(5, e, rel_tol=TOLERANCE)
