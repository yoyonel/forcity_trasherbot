"""

"""
import numpy as np
#
from forcity.trasherbot.model.board import Board
from forcity.trasherbot.model.trash import Trash


object_to_str = {
    Trash: 'T',
}


def debug_show_board(b: Board) -> np.ndarray:
    # https://stackoverflow.com/questions/35215161/most-efficient-way-to-map-function-over-numpy-array
    f = np.vectorize(lambda o: 'T' if type(o) == Trash else '.')(b.field.field)
    #
    f[b.bot.position.ndarray_indices] = 'B' + ('T' if b.field.is_trash(b.bot.position) else '')
    return f
