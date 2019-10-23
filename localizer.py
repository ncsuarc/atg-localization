from typing import Tuple, Optional
import math

STEP_SIZE = 1
NUM_STEPS = 200


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
    v_north = math.sin(angle_north) * STEP_SIZE
    v_east = math.sin(angle_east) * STEP_SIZE
    v_alt = math.cos(angle_north) * math.cos(angle_east) * -STEP_SIZE

    for _ in range(NUM_STEPS):
        if pos_agl <= 0:
            return pos_north, pos_east
        pos_north += v_north
        pos_east += v_east
        pos_agl += v_alt
    return None


print(find_ground(10, 0, 0, 0, math.asin(5 / math.sqrt(125))))
