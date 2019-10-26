from localizer import find_ground
import math


TOLERANCE = 0.5


def test_timeout():
    assert find_ground(10000000, 0, 0) is None

    assert find_ground(10, math.pi / 2, 0) is None

    assert find_ground(10, 0, math.pi / 2) is None


def test_on_ground():
    """
    Test when the gimbal is exactly on the ground.

    Detects off by one errors.
    """
    assert find_ground(0, 0, 0) == (0, 0)
    assert find_ground(0, math.pi / 2, 0) == (0, 0)
    assert find_ground(0, 0, math.pi / 2) == (0, 0)


def test_one_angle():
    # rotate east
    n, e = find_ground(10, 0, math.asin(5 / math.sqrt(10 ** 2 + 5 ** 2)))
    assert math.isclose(0, n, rel_tol=TOLERANCE)
    assert math.isclose(5, e, rel_tol=TOLERANCE)

    # rotate north
    n, e = find_ground(100, math.asin(20 / math.sqrt(100 ** 2 + 20 ** 2)), 0)
    assert math.isclose(20, n, rel_tol=TOLERANCE)
    assert math.isclose(0, e, rel_tol=TOLERANCE)


def test_two_angles():
    n, e = find_ground(58.57, 0.6374, 0.8477)
    assert math.isclose(43.37, n, rel_tol=TOLERANCE)
    assert math.isclose(82.59, e, rel_tol=TOLERANCE)

    n, e = find_ground(128.5, 0.08423, 0.8351)
    assert math.isclose(10.86, n, rel_tol=TOLERANCE)
    assert math.isclose(142.5, e, rel_tol=TOLERANCE)

    # Combined angle points up and never hits ground
    assert find_ground(48.13, 1.248, 0.7715) is None
