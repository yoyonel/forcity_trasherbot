"""

"""
from bresenham import bresenham
from dataclasses import dataclass
import numpy as np
import random
#
from forcity.trasherbot.model.position import Position


@dataclass
class Bot:
    # `Map` properties (from json configuration: {'bot'})
    position: Position

    @classmethod
    def from_json(cls, json_bot) -> 'Bot':
        """
        pre-requisite: json_map is a valide json datas for `bot` (see `load_config:validate_config()`)

        :param json_bot:
        :return:
        """
        return cls(position=Position.from_json(json_bot))

    @property
    def ndarray_indices(self):
        return self.position.ndarray_indices

    def move(self, target: Position, max_range: int):
        """
        Action: "Move to Target"
        If the target is too far, the robot (navigation) use a Bresenham rasterisation as far that it can
        -> a position at `max_range` (Manhantan's) distance.

        https://pypi.org/project/bresenham/
        https://docs.google.com/drawings/d/1XBXvOzsdl3yOGeUg8z3QBm9slOmc6DcBFFy2oaE52dc/edit?usp=sharing

        :param target:
        :param max_range: information from `Map`
        """
        next_bot_pos = target

        # test if target is out the reach
        motion_vector = next_bot_pos - self.position
        if motion_vector.distance() > max_range:
            # TODO: I.A => more stategies are possible to choose different paths (with different potentials "gains")
            # [HYP] If the bot want to go too far, we choose to move at range limit
            dist_bresenham_to_bot = 0
            bresenham_pos = self.position
            # loop through raster position with Bresenham algorithm
            for bresenham_pos in map(lambda bp: Position(*bp), bresenham(*self.position, *target)):
                # for each position: Test if the distance (bot to bresenham position) is greater than max_range
                dist_bresenham_to_bot = (self.position - bresenham_pos).distance()
                if dist_bresenham_to_bot >= max_range:
                    break
            next_bot_pos = bresenham_pos
            # the last (Bresenham) position can be outer the max_range limit
            # (because Bresenham "allow" diagonal movement)
            if dist_bresenham_to_bot > max_range:
                # choose randomly valid neighbors of this last Bresenham position
                if random.random() > 0.5:
                    next_bot_pos = bresenham_pos - Position(np.sign(motion_vector.x_pos), 0)
                else:
                    next_bot_pos = bresenham_pos - Position(0, np.sign(motion_vector.y_pos))

        self.position = next_bot_pos
