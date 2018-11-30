"""

"""
import json
from jsonschema import validate
from typing import TextIO


# https://github.com/Julian/jsonschema
schema_for_boards = {
    "type": "object",
    "properties": {
        "map": {
            "type": "object",
            "properties": {
                "x_max": {"type": "number"},
                "y_max": {"type": "number"},
                "max_range": {"type": "number"},
                "max_rounds": {"type": "number"},
            }
        },
        "bot": {
            "type": "object",
            "properties": {
                "x_pos": {"type": "number"},
                "y_pos": {"type": "number"},
            }
        },
        "trash": {
            # https://json-schema.org/understanding-json-schema/reference/array.html
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "x_pos": {"type": "number"},
                    "y_pos": {"type": "number"},
                }
            }
        }
    },
}


def validate_config(json_board: dict):
    """

    :param json_board:
    :return:
    """
    validate(json_board, schema_for_boards)


def load_config(json_file: TextIO, validate_schema: bool = True) -> dict:
    """

    :param json_file:
    :param validate_schema:
    :return:
    """
    json_config = json.load(json_file)

    # Load datas
    if validate_schema:
        validate_config(json_config)

    return json_config
