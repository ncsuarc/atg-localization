from typing import Tuple, Optional
import math

STEP_SIZE = 1
""" Assume we step 1 meter toward target until we hit the ground """

NUM_STEPS = 200
""" The maximum number of steps before test fails """


def find_ground(
    height: float, angle_north: float, angle_east: float
) -> Optional[Tuple[float, float]]:
    """
    Return the north and east distance from target to gimble.

    Let height, north angle, and east angle be given by the caller, and assume the 
    gimble starts at location <0, 0, 0> (<north, east, down>). We then image a 
    light ray takes 1 meter steps from the gimble towards the target. As we step, 
    we add the change in distance, relative to the respective plane, to the current 
    position of the light ray. Once the downward position of the ray is greater 
    or equal to the height of the gimble, we return the north and east distance 
    from the gimble to the light ray. 

    Args:
        height: altitude of gimble
        angle: North, East radians
    """
    pos_north = 0.0 # meters
    pos_east = 0.0 # meters
    pos_down = 0.0 # meters

    step_north = math.sin(angle_north) * STEP_SIZE # meters
    step_east = math.sin(angle_east) * STEP_SIZE # meters
    step_down = math.cos(angle_north) * math.cos(angle_east) * STEP_SIZE # meters

    for _ in range(NUM_STEPS):
        if pos_down > height:
            return pos_north, pos_east
        pos_north += step_north
        pos_east += step_east
        pos_down += step_down
    return None
