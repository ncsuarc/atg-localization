from localizer import find_ground
import math

TOLERANCE = 0.5

def test_too_high_in_the_sky():
    assert find_ground(10000000,0,0,0,0) is None

def test_straight_up_north():
    assert find_ground(10,0,0,math.pi/2,0) is None

def test_north_east():
    assert find_ground(10,0,0,0,math.pi/2) is None

def test_on_the_ground_all_zeros():
    assert find_ground(0,0,0,0,0) == (0,0)

def test_on_the_ground_at_10_10():
    assert find_ground(0,10,10,0,0) == (10,10)

def test_basic1():
    n, e = find_ground(10,0,0,0,math.asin(5/math.sqrt(125)))
    assert math.isclose(0, n, rel_tol=TOLERANCE)
    assert math.isclose(5, e, rel_tol=TOLERANCE)