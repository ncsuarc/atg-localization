import pint
from typing import Tuple, Optional
import math

ureg = pint.UnitRegistry()


STEP_SIZE = 1 * ureg.meter
NUM_STEPS = 200


@ureg.wraps(
    (ureg.meter, ureg.meter),  # return
    (ureg.meter, ureg.meter, ureg.meter, ureg.radian, ureg.radian),  # param
)
def find_ground(
    pos_agl: float,
    pos_north: float,
    pos_east: float,
    angle_north: float,
    angle_east: float,
) -> Optional[Tuple[float, float]]:
    """
    Args:
        agl: AGL altitude
        pos: North, East coordinates
        angle: North, East radians
    """
    v_north = STEP_SIZE * math.sin(angle_north)
    v_east = STEP_SIZE * math.sin(angle_east)
    v_alt = -STEP_SIZE * math.cos(angle_north) * math.cos(angle_east)

    for i in range(NUM_STEPS):
        if pos_agl <= 0:
            return pos_north, pos_east
        pos_north += v_north
        pos_east += v_east
        pos_agl += v_alt
    return None
