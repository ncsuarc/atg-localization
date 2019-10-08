import pint
from typing import Tuple
import math

ureg = pint.UnitRegistry()


STEP_SIZE = 1 * ureg.meter
NUM_STEPS = 200

@ureg.wraps((ureg.meter, ureg.meter), (ureg.meter, ureg.radian, ureg.radian))
def find_ground(agl: float, east_angle: float, north_angle: float, pos: float) -> Tuple[float, float]:
    v_east = STEP_SIZE * math.sin(east_angle)
    v_north = STEP_SIZE * math.sin(north_angle)
    v_alt = -STEP_SIZE * math.cos(north_angle) * math.cos(east_angle)
    pos_north, pos_east, pos_alt = pos

    for i in range(NUM_STEPS):
        if pos_alt <= 0:
            return pos_north, pos_east
        pos_north += v_north
        pos_east += v_east
        pos_alt += v_alt
    return None
        
