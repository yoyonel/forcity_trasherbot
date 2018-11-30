"""

"""
from forcity.trasherbot.model.position import Position


def get_bot_position(json_config) -> Position:
    return Position.from_json(json_config['bot'])


def test_instantiate_position_from_json(test_datas_json_config):
    position = get_bot_position(test_datas_json_config)
    # load json datas
    assert position.x_pos == test_datas_json_config['bot']['x_pos']
    assert position.y_pos == test_datas_json_config['bot']['y_pos']


def test_position_ndarray_indices(test_datas_json_config):
    position = get_bot_position(test_datas_json_config)
    # convert positions to (numpy) 2d-array indices
    nd_array_indice_i = test_datas_json_config['bot']['x_pos'] - 1
    nd_array_indice_j = test_datas_json_config['bot']['y_pos'] - 1
    assert position.i == nd_array_indice_i
    assert position.j == nd_array_indice_j
    assert position.ndarray_indices == (nd_array_indice_i, nd_array_indice_j)


def test_addition_positions(test_datas_json_config):
    position = get_bot_position(test_datas_json_config)
    double_position = Position(x_pos=test_datas_json_config['bot']['x_pos']*2,
                               y_pos=test_datas_json_config['bot']['y_pos']*2)
    # __add__
    assert position + position == double_position
    # __radd__
    assert sum([position] * 2) == double_position


def test_subtract_positions(test_datas_json_config):
    position = get_bot_position(test_datas_json_config)
    origin = Position(x_pos=0, y_pos=0)
    # __sub__
    assert position - position == origin


def test_neg_position(test_datas_json_config):
    position = get_bot_position(test_datas_json_config)
    # __neg__
    assert -position == Position(x_pos=-test_datas_json_config['bot']['x_pos'],
                                 y_pos=-test_datas_json_config['bot']['y_pos'])


def test_distance(test_datas_json_config):
    position = get_bot_position(test_datas_json_config)
    # distance
    assert position.distance() == (
            abs(test_datas_json_config['bot']['x_pos']) + abs(test_datas_json_config['bot']['y_pos']))
