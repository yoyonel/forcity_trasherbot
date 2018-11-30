"""

"""
from dataclasses import dataclass
import logging
import random
from typing import Optional, Generator
#
from forcity.trasherbot.model.bot import Bot
from forcity.trasherbot.model.position import Position
from forcity.trasherbot.model.map import Map
from forcity.trasherbot.model.trash import Trash, Trashes


logger = logging.getLogger(__name__)


@dataclass
class Board:
    # `Board` objects
    field: Map
    trashes: Trashes
    bot: Bot

    raise_exception_on_validation: bool = False

    def validate(self):
        for trash in self.trashes:
            if not self.field.is_in_grid(trash.position):
                message = f"Trash (position={trash.position}) not in Map (dimension={self.field.dimension})"
                logger.warning(message)
                if self.raise_exception_on_validation:
                    raise ValueError(message)
                # remove the trash
                self.trashes.remove(trash)

    def __post_init__(self):
        self.validate()
        for trash in self.trashes:
            self.field.add_trash(trash)

    @classmethod
    def from_json(cls, json_config: dict, **kwargs) -> 'Board':
        """
        pre-requisite: json_config is a valide json datas configuration (see `load_config:validate_config()`)

        :param json_config:
        :return:
        """
        return cls(
            field=Map.from_json(json_config['map']),
            bot=Bot.from_json(json_config['bot']),
            trashes=Trashes.from_json(json_config['trash']),
            **kwargs,
        )

    @property
    def nb_trashes_remaining(self) -> int:
        return len(self.trashes)

    def gen_propagate_trashes(self) -> Generator[Trash, None, None]:
        # loop on propagated trashes
        for trash_propaged in self.trashes.propage():
            try:
                # choose randomly a available/free neighboor's position around the propagated trash
                trash_position_to_propagate = random.choice(list(self.field.free_neighbors(trash_propaged.position)))
            except IndexError:
                # no propagation from this trash because no available position to propagate
                continue
            # build the new propagated trash
            trash_to_propagate = Trash(position=trash_position_to_propagate)
            # add this new trash to `self.field[Map]` and `self.trashes[Trashes]`
            self.field.add_trash(trash_to_propagate)
            self.trashes.add(trash_to_propagate)
            # yield the new trash (useful for logs)
            yield trash_to_propagate

    def move_bot(self, target: Position, collect_trash: bool = True) -> bool:
        """
        Action: Move robot to an aim (target) and (potentially) collect trash if it can.
        This action return if the robot collect or not a trash.

        :param target:
        :param collect_trash:
        :return:
        """
        trash_collected = False
        # order the robot to move to the target as far as it can
        self.bot.move(target, self.field.max_range)
        if collect_trash:
            trash_to_collect = self.field.get_trash(self.bot.position)
            if trash_to_collect is not None:
                self.trashes.remove(trash_to_collect)
                self.field.remove_trash(trash_to_collect)
                trash_collected = True

        return trash_collected

    def find_closest_trash(self) -> Optional[Trash]:
        try:
            # TODO: Need to optimize ! Inefficient ! (but very simple :p)
            # sort ALL trashes by distance from the bot and select (on of/the first) the closest
            return sorted(
                self.trashes,
                key=lambda trash: (trash.position - self.bot.position).distance()
            )[0]
        except IndexError:
            return None
