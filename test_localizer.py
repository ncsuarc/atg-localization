from localizer import find_ground
import math


TOLERANCE = 0.5


def test_timeout():
    assert find_ground(10000000, 0, 0) is None

    assert find_ground(10, math.pi / 2, 0) is None

    assert find_ground(10, 0, math.pi / 2) is None


def test_simple():
    assert find_ground(0, 0, 0) == (0, 0)


def test_complex():
    """
    Check that find_ground returns a coordinates within 0.5 meters of target
    
    We started with a rotation matrix formed by combining rotation about the North
    and East axes. Then, we multiplied the matrix by the vector <0,0,1>, finding 
    where the camera was pointing. We tested if this vector had the same direction 
    as the offset vector from the gimbal to the ground. In other words, the vector 
    we tested against was a unit vector pointed towards the ground. This forms a 
    solveable system of equations for phi and theta, which can be used to generate 
    test cases. We solved manually, but then we used WolframAlpha to solve the 
    system of equations.

    URL for math: solve for \theta and \phi \:\frac{x}{\sqrt{\left(x^2 + y^2 + 
    z^2\right)}}=sin\left(\theta \right)cos\left(\phi \right),\:\frac{y}{\sqrt
    {\left(x^2 + y^2 + z^2\right)}}=sin\left(\phi \right),\:\frac{z}{\sqrt{\left
    (x^2 + y^2 + z^2\right)}}=cos\left(\theta \right)cos\left(\phi \right) 
    - Wolfram|Alpha

    Unit tests were generating by forming a (5,3) Numpy matrix and filling the 
    first 3 rows with values between 0 and 150. The remaining two rows (phi 
    and theta) were filled out with a list comprehension using the formula 
    derived above.

    We then took the values from the Numpy matrix and hardcoded them into
    a few tests.
    """
    n, e = find_ground(10, 0, math.asin(5 / math.sqrt(125)))
    assert math.isclose(0, n, rel_tol=TOLERANCE)
    assert math.isclose(5, e, rel_tol=TOLERANCE)

    n, e = find_ground(58.57, 0.6374, 0.8477)
    assert math.isclose(43.37, n, rel_tol=TOLERANCE)
    assert math.isclose(82.59, e, rel_tol=TOLERANCE)

    n, e = find_ground(128.5, 0.08423, 0.8351)
    assert math.isclose(10.86, n, rel_tol=TOLERANCE)
    assert math.isclose(142.5, e, rel_tol=TOLERANCE)

    # Combined angle points up and never hits ground
    assert find_ground(48.13, 1.248, 0.7715) is None
