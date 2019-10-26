from typing import Tuple, Optional
import math

STEP_SIZE = 1
NUM_STEPS = 200


def find_ground(
    height: float, angle_north: float, angle_east: float
) -> Optional[Tuple[float, float]]:
    """
    Args:
        agl: AGL altitude
        pos: North, East coordinates
        angle: North, East radians
    """
    pos_north = 0.0
    pos_east = 0.0
    pos_down = 0.0

    step_north = math.sin(angle_north) * STEP_SIZE
    step_east = math.sin(angle_east) * STEP_SIZE
    step_down = math.cos(angle_north) * math.cos(angle_east) * STEP_SIZE

    for _ in range(NUM_STEPS):
        if pos_down >= height:
            return pos_north, pos_east
        pos_north += step_north
        pos_east += step_east
        pos_down += step_down
    return None
