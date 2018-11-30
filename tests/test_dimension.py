"""

"""
from typing import Dict, Tuple
#
from forcity.trasherbot.model.dimension import Dimension


def load_json_dimension(json_config) -> Tuple[Dict, Dimension]:
    json_map = json_config['map']
    dimension = Dimension.load(json_config['map'])
    return json_map, dimension


def test_instantiate_dimension_from_json(test_datas_json_config):
    json_map, dimension = load_json_dimension(test_datas_json_config)
    assert dimension.x_max == json_map['x_max']
    assert dimension.y_max == json_map['y_max']


def test_dimension_iter(test_datas_json_config):
    json_map, dimension = load_json_dimension(test_datas_json_config)
    assert list(dimension) == [json_map['x_max'], json_map['y_max']]
