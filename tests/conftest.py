# coding=utf-8
"""

"""
import pytest
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(funcName)s - %(levelname)s - %(message)s',
)


@pytest.fixture(autouse=True)
def setup_doctest_logger(log_level: int = logging.DEBUG):
    """

    :param log_level:
    :return:

    """
    if is_pycharm_running():
        logger_add_streamhandler_to_sys_stdout()
    logger.setLevel(log_level)


def is_pycharm_running() -> bool:
    if ('docrunner.py' in sys.argv[0]) or ('pytest_runner.py' in sys.argv[0]):
        return True
    else:
        return False


def logger_add_streamhandler_to_sys_stdout():
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(stream_handler)


@pytest.fixture(scope="session", autouse=True)
def test_datas_json_config():
    """
    :return:
    """
    return {
        "map": {
            "x_max": 10,
            "y_max": 6,
            "max_range": 4,
            "max_rounds": 50
        },
        "bot": {
            "x_pos": 1,
            "y_pos": 1
        },
        "trash": [
            {
                "x_pos": 4,
                "y_pos": 5
            },
            {
                "x_pos": 10,
                "y_pos": 1
            },
            {
                "x_pos": 10,
                "y_pos": 3
            }
        ]
    }
