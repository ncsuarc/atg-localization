import math


def p2a(x, y, width, height, vfov, hfov):
    """
    Returns the x and y angles for a given pixel

    Args: 
        x: horizontal pixel position
        y: vertical pixel position
        width: number of pixels in the horizontal direction
        height: number of pixels in vertical direction
        vfov: angle of vertical field of view
        hfov: angle of horizontal field of view

    Units:
        h_angle: radians
        v_angle: radians
    """

    h_angle = math.radians(((x / width) - 0.5) * hfov)
    v_angle = math.radians(((y / height) - 0.5) * vfov)
    return h_angle, v_angle
