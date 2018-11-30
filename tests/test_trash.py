"""

"""
import logging
#
from forcity.trasherbot.model.trash import Trash, Trashes


logger = logging.getLogger(__name__)


def test_instantiate_trash_from_json(test_datas_json_config):
    json_trash = test_datas_json_config['trash'][0]

    # load json trash
    trash = Trash.from_json(json_trash)
    assert trash.position.x_pos == json_trash['x_pos']
    assert trash.position.y_pos == json_trash['y_pos']


def test_instantiate_trashes_from_json(test_datas_json_config):
    json_trashes = test_datas_json_config['trash']

    # load json trashes
    trashes = Trashes.from_json(json_trashes)

    assert len(trashes.trashes) == len(json_trashes)
    assert all(isinstance(x, Trash) for x in trashes.trashes)


def test_trashes_iter(test_datas_json_config):
    json_trashes = test_datas_json_config['trash']

    # load json trashes
    trashes = Trashes.from_json(json_trashes)
    # test __iter__
    assert list(iter(trashes)) == trashes.trashes


def test_trashes_len(test_datas_json_config):
    json_trashes = test_datas_json_config['trash']

    # load json trashes
    trashes = Trashes.from_json(json_trashes)
    # test __len__
    assert len(trashes) == len(trashes.trashes)


def test_thrashs_add():
    # TODO: write unit test!
    logger.warning("No tests!")


def test_thrashs_remove():
    # TODO: write unit test!
    logger.warning("No tests!")


def test_thrashs_propage():
    # TODO: write unit test!
    logger.warning("No tests!")
