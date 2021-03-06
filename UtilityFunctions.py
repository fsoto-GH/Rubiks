from CONSTANTS import DOT_RAD
from Transformations import ROTATIONS

from numpy import dot, matrix, pi, array


def as_dot(p, rad=DOT_RAD):
    """
    This returns the diagonal coordinates necessary
    to compose the circle of a given radius.

    :param matrix p: point to convert
    :param int rad: radius for the circle

    :return: a list of edges
    :rtype: tuple
    """
    return int(p[0]) - rad, int(p[1]) - rad, int(p[0]) + rad, int(p[1]) + rad


def rot(p, theta, rotation):
    """
    This method rotates a given point by the given angle and
    in the direction specified.

    :param matrix p: point to rotate
    :param float theta: angle to rotate by
    :param str rotation: x, y, or z

    :return: a matrix representing the points new position
    :rtype: matrix
    """
    return dot(ROTATIONS[rotation](theta), p)


def rot_x(p, theta=90):
    """
    This rotates a point in the x-axis by theta.

    :param matrix p: point to rotate
    :param float theta: angle to rotate by

    :return: a matrix representing the points new position
    :rtype: matrix
    """
    return rot(p, theta, 'x')


def rot_y(p: matrix, theta=90):
    """
    This rotates a point in the y-axis by theta.

    :param matrix p: point to rotate
    :param float theta: angle to rotate by

    :return: a matrix representing the points new position
    :rtype: matrix
    """
    return rot(p, theta, 'y')


def rot_z(p, theta=90):
    """
    This rotates a point in the z-axis by theta.

    :param matrix p: point to rotate
    :param float theta: angle to rotate by

    :return: a matrix representing the points new position
    :rtype: matrix
    """
    return rot(p, theta, 'z')


def sign_p(v):
    """
    This is a positive-biased version of a sign function.
    This returns -1 if v < 0 else 1.

    :param int v: number to compare on
    :rtype: int
    """
    return -1 if v < 0 else 1


def adjust_theta(v):
    if -2 * pi <= v <= 2 * pi:
        return v
    elif 2 * pi < v:
        return -2 * pi
    else:
        return 2 * pi


def to_rad(deg):
    return deg * pi / 180


def to_deg(rad):
    return rad * 180 / pi


def project(p, x_rad, y_rad, z_rad):
    _p = rot_x(p, y_rad)
    _p = rot_y(_p, x_rad)
    _p = rot_z(_p, z_rad)
    return _p


# Cube
def gen_cube(width, height, depth, x_offset: float = 0, y_offset: float = 0, z_offset: float = 0):
    width /= 2
    height /= 2
    depth /= 2
    return array([matrix([[-width + x_offset], [-height + y_offset], [depth + z_offset]]),
                  matrix([[width + x_offset], [-height + y_offset], [depth + z_offset]]),
                  matrix([[-width + x_offset], [height + y_offset], [depth + z_offset]]),
                  matrix([[width + x_offset], [height + y_offset], [depth + z_offset]]),
                  matrix([[-width + x_offset], [height + y_offset], [-depth + z_offset]]),
                  matrix([[width + x_offset], [-height + y_offset], [-depth + z_offset]]),
                  matrix([[-width + x_offset], [-height + y_offset], [-depth + z_offset]]),
                  matrix([[width + x_offset], [height + y_offset], [-depth + z_offset]])])