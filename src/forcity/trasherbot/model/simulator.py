"""

"""
import logging
from typing import TextIO
#
from forcity.trasherbot.model.board import Board
from forcity.trasherbot.tools.load_config import load_config


logger = logging.getLogger('forcity.trasherbot.simulator')


def simulate(json_config: TextIO) -> int:
    """

    :param json_config:
    :return:
    """
    state = "init game"
    json_config = load_config(json_config)
    board = Board.from_json(json_config)
    #
    for i, trash in enumerate(board.trashes, start=1):
        logger.info(f"{state}: trash pop, remaining {i}")

    # ~ Game Loop
    i_round = 1
    for i_round in range(1, board.field.max_rounds+1):
        state = f"Round {i_round}/{board.field.max_rounds}"

        closest_trash = board.find_closest_trash()
        if closest_trash is not None:
            logger.debug(f"Closest trash to bot: {closest_trash}")
            trash_collected = board.move_bot(closest_trash.position)
            if trash_collected:
                logger.info(f"{state}: trash collected, remaining {board.nb_trashes_remaining}")
            if len(board.trashes) == 0:
                break
        logger.debug(f"Bot position: {board.bot.position}")
        for _ in board.gen_propagate_trashes():
            logger.info(f"{state}: trash pop, remaining {len(board.trashes)}")

    # last log for finishing: success or game_over depending of the remaining trashes in field/map
    if board.nb_trashes_remaining == 0:
        logger.info(f"success. Collected all trashes in {i_round} round{'s' if i_round > 1 else ''}")
    else:
        logger.info(f"game over. {board.nb_trashes_remaining} trashes remaining "
                    f"after {i_round} round{'s' if i_round > 1 else ''}")

    # Consigne: "La commande python fournie prend en argument ce fichier et renvoie le nombre de tours
    # mis pour récolter tous les déchets, ou le nombre maximum de tour si celui-ci est atteint."
    return i_round
