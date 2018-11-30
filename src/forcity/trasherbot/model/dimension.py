"""

"""
from dataclasses import dataclass


@dataclass
class Dimension:
    x_max: int
    y_max: int

    @classmethod
    def load(cls, json_dimension: dict) -> 'Dimension':
        return cls(json_dimension['x_max'], json_dimension['y_max'])

    def __iter__(self):
        yield self.x_max
        yield self.y_max
