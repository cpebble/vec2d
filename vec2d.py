""" A simple helper for using 2d vectors 
Copyright @Christian Påbøl Jacobsen, 2019
GPL License(code as of 27/05/19 not yet publicly available)
"""
from __future__ import annotations  # Bleeding edge!!
from math import sin, cos, atan2
import numpy as np
from numbers import Number


class Vec2d():
    def __init__(self, x: Number, y: Number) -> None:
        self.internal = np.array([x, y], dtype=np.float)

    @property
    def x(self) -> Number:
        return self.internal[0]

    @property
    def y(self) -> Number:
        return self.internal[1]

    def __add__(self, other: Vec2d) -> Vec2d:
        """ Vector addition and scalar addition"""
        if isinstance(other, Vec2d):
            result = self.internal + other.internal
            return Vec2d(x=result[0], y=result[1])
        if isinstance(other, Number):
            """ scalar addition """
            result = self.internal + other
            return Vec2d(x=result[0], y=result[1])

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2d(x=self.x + other.x, y=self.y + other.y)

    def __mod__(self, scalar: Number):
        return Vec2d(x=self.x % scalar, y=self.y % scalar)

    def __iadd__(self, other):
        self = self.__add__(other)
        return self

    def __sub__(self, other):
        """ Vector substraction """
        if isinstance(other, Vec2d):
            return Vec2d(x=self.x - other.x, y=self.y - other.y)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2d(x=self.x - other.x, y=self.y - other.y)

    def __isub__(self, other):
        self = self.__sub__(other)
        return self

    def __mul__(self, other):
        """ Scalar_multiplication """
        return Vec2d(self.x * other, self.y * other)

    def __truediv__(self, other):
        """ Scalar division """
        return Vec2d(self.x / other, self.y / other)

    def __setstate__(self, state):
        """ Backwards compatibility """
        self.__dict__.update(state)
        if not "internal" in state and ('x' in state and 'y' in state):
            self.internal = np.array([state['x'], state['y']], dtype=np.float)

    def rotate(self, angle):
        """ Rotate a vector around the 0,0 Origin point(cw) """
        co, si = np.cos(angle), np.sin(angle)
        P = np.array([[co, si], [-si, co]])
        rotated = P @ self.internal.T
        # Transposed to avoid numpy bug in 1.16.4
        return Vec2d(rotated.T[0], rotated.T[1])

    def normalize(self):
        if self.length == 0:
            return self
        return self / self.length

    def dot_product(self, other):
        if not isinstance(other, Vec2d):
            raise NotImplementedError("What u doin o.O Not a vec2d")
        return np.dot(self.internal, other.internal)

    @property
    def angle(self):
        """ returns the angle in radians """
        return atan2(self.y, self.x)

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
