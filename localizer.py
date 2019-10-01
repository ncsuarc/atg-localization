import pint
from typing import Tuple
import math

ureg = pint.UnitRegistry()


STEP_SIZE = 1 * ureg.meter


@ureg.wraps((ureg.meter, ureg.meter), (ureg.meter, ureg.radian, ureg.radian))
def find_ground(agl: float, east_angle: float, north_angle: float) -> Tuple[float, float]:
    v_east = STEP_SIZE * math.sin(east_angle)
    v_north = STEP_SIZE * math.sin(north_angle)
    v_alt = -1 * math.cos(north_angle) * math.cos(east_angle)

    # TODO: Do calculations
