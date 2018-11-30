"""

"""
from dataclasses import dataclass


@dataclass
class Position(object):
    # `Position` properties (from json configuration)
    x_pos: int
    y_pos: int

    @classmethod
    def from_json(cls, json_position: dict) -> 'Position':
        return cls(json_position['x_pos'], json_position['y_pos'])

    @property
    def i(self):
        return self.x_pos - 1

    @property
    def j(self):
        return self.y_pos - 1

    @property
    def ndarray_indices(self):
        return self.i, self.j

    def __add__(self, other):
        return Position(
            x_pos=self.x_pos + other.x_pos,
            y_pos=self.y_pos + other.y_pos,
        )

    def __sub__(self, other):
        return Position(
            x_pos=self.x_pos - other.x_pos,
            y_pos=self.y_pos - other.y_pos,
        )

    def __neg__(self):
        return Position(x_pos=-self.x_pos, y_pos=-self.y_pos)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iter__(self):
        yield self.x_pos
        yield self.y_pos

    def distance(self) -> int:
        """
        https://en.wikipedia.org/wiki/Taxicab_geometry

        :return:
        """
        return abs(self.x_pos) + abs(self.y_pos)
