"""

"""
from dataclasses import dataclass
import logging
import numpy as np
from typing import Iterator, List
#
from forcity.trasherbot.model.position import Position


logger = logging.getLogger(__name__)


@dataclass
class Trash:
    # `Trash` properties (from json configuration: {'trash'})
    position: Position

    @classmethod
    def from_json(cls, json_trash: dict) -> 'Trash':
        """
        pre-requisite: json_trashes is a valide json datas for `trashes` (see `load_config:validate_config()`)

        :param json_trash:
        :return:
        """
        return Trash(Position(json_trash['x_pos'], json_trash['y_pos']))


@dataclass
class Trashes:
    # `Trashes` aggregation entities (from json configuration: {'trash'})
    trashes: List[Trash]
    # TODO: [DESIGN] Could been an attribute of json datas for {'trash'}
    propagation_rate: float = 0.25

    @classmethod
    def from_json(cls, json_trashes) -> 'Trashes':
        """
        pre-requisite: json_trashes is a valide json datas for `trashes` (see `load_config:validate_config()`)

        :param json_trashes:
        :return:
        """
        # return cls(trashes=list(map(Trash.from_json, json_trashes)))
        trashes = cls([])
        for json_trash in json_trashes:
            trashes.add(Trash.from_json(json_trash))
        return trashes

    def __iter__(self) -> Iterator[Trash]:
        return iter(self.trashes)

    def __len__(self) -> int:
        return len(self.trashes)

    def add(self, trash: Trash):
        self.trashes.append(trash)

    def remove(self, trash: Trash):
        self.trashes.remove(trash)

    def propage(self) -> List[Trash]:
        return np.array(self.trashes)[np.random.rand(len(self.trashes)) <= self.propagation_rate]
