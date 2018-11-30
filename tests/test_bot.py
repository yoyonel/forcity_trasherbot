"""

"""
from typing import Dict, Tuple
#
from forcity.trasherbot.model.bot import Bot
from forcity.trasherbot.model.position import Position


def load_json_bot(json_config: dict) -> Tuple[Dict, Bot]:
    json_bot = json_config['bot']
    bot = Bot.from_json(json_bot)
    return json_bot, bot


def test_instantiate_bot_from_json(test_datas_json_config: dict):
    json_bot, bot = load_json_bot(test_datas_json_config)
    # test load json bot position
    assert bot.position == Position(x_pos=json_bot["x_pos"], y_pos=json_bot["y_pos"])


def test_bot_position_ndarray_indice(test_datas_json_config: dict):
    json_bot, bot = load_json_bot(test_datas_json_config)
    # test bot position into ndarray indices
    assert bot.ndarray_indices == (json_bot["x_pos"] - 1, json_bot["y_pos"] - 1)


def test_move_bot(test_datas_json_config: dict):
    json_bot, bot = load_json_bot(test_datas_json_config)

    max_range = 3

    # TODO: Find more 'clever' tests here :p
    tests_targets = [
        (Position(5, 4), max_range),
        (Position(0, 5), max_range),
        (Position(5, -4), max_range),
        (Position(0, -4), max_range),
        (Position(-5, -4), max_range),
        (Position(-5, 0), max_range),
        (Position(-5, 4), max_range),
        #
        (Position(1, 2), max_range),
        (Position(1, 1), max_range),
        (Position(0, 2), max_range),
    ]
    #
    bot_origin_position = bot.position
    for target_offset, max_range in tests_targets:
        bot.move(bot.position + target_offset, max_range)
        assert (bot_origin_position - bot.position).distance() == min(max_range, target_offset.distance())
        bot.position = bot_origin_position
