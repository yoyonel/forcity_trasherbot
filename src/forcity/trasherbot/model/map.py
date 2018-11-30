"""

"""
from dataclasses import dataclass
import logging
import numpy as np
from typing import Iterator, Optional
#
from forcity.trasherbot.model.dimension import Dimension
from forcity.trasherbot.model.position import Position
from forcity.trasherbot.model.trash import Trash, Trashes


logger = logging.getLogger(__name__)


neighbors_dir = [
    Position(-1, 0),
    Position(+1, 0),
    Position(0, -1),
    Position(0, +1),
]


@dataclass
class Map:
    # `Map` properties (from json configuration: {'map'})
    dimension: Dimension
    max_range: int
    max_rounds: int
    #
    field: np.ndarray

    @classmethod
    def from_json(cls, json_map: dict) -> 'Map':
        """
        pre-requisite: json_map is a valide json datas for `map` (see `load_config:validate_config()`)

        :param json_map:
        :return:

        """
        dimension = Dimension.load(json_map)
        return cls(
            dimension=dimension,
            max_range=json_map['max_range'],
            max_rounds=json_map['max_rounds'],
            field=np.empty(tuple(dimension), dtype=object)
        )

    def add_trash(self, trash: Trash):
        self.field[trash.position.ndarray_indices] = trash

    def add_trashes(self, trashes: Trashes):
        map(self.add_trash, trashes)

    def remove_trash(self, trash: Trash):
        self.field[trash.position.ndarray_indices] = None

    def is_in_grid(self, position: Position) -> bool:
        return (1 <= position.x_pos <= self.dimension.x_max) and (1 <= position.y_pos <= self.dimension.y_max)

    def is_trash(self, position: Position) -> bool:
        return isinstance(self.field[position.ndarray_indices], Trash)

    def is_not_trash(self, position: Position) -> bool:
        return not self.is_trash(position)

    def get_trash(self, position: Position) -> Optional[Trash]:
        return self.field[position.ndarray_indices]

    def free_neighbors(self, position: Position) -> Iterator[Position]:
        # Return iterator on free/available (not trashs) neighbors's positions (in cardinal direction)
        return filter(
            self.is_not_trash,
            filter(
                self.is_in_grid,
                [
                    position + neighboor_dir
                    for neighboor_dir in neighbors_dir
                ]
            )
        )
