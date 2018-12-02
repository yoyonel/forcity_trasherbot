#!/usr/bin/env python
"""

"""
import argparse
import logging
import os
import pkg_resources
import signal
import sys
#
from forcity.trasherbot.model.simulator import simulate


logger = logging.getLogger('forcity.trasherbot.app')

SIGNALS = [signal.SIGINT, signal.SIGTERM]


def process(args) -> int:
    """

    :param args:
    :return:
    """
    def _signal_handler(_sig, _):
        """ Empty signal handler used to override python default one """
        logger.info("sig: {} intercepted. Closing application.".format(_sig))
        # https://stackoverflow.com/questions/73663/terminating-a-python-script
        sys.exit()

    # Signals HANDLER (to exit properly)
    for sig in SIGNALS:
        signal.signal(sig, _signal_handler)

    return simulate(args.json_config, args.show_map_at_each_round)


def return_result(result: int):
    """
    Consigne: "La commande python fournie prend en argument ce fichier et renvoie le nombre de tours mis
    pour récolter tous les déchets, ou le nombre maximum de tour si celui-ci est atteint."

    :param result:
    :return:
    """
    sys.stdout.write(str(result))
    sys.stdout.flush()


def build_parser(parser=None, **argparse_options):
    """
    Args:
        parser (argparse.ArgumentParser):
        **argparse_options (dict):
    Returns:
    """
    if parser is None:
        parser = argparse.ArgumentParser(**argparse_options)

    argparse_default = "(default=%(default)s)."

    parser.add_argument('json_config',
                        default=os.environ.get('FORCITY_TRASHERBOT_APP_JSON', 'data/config_00.json'),
                        type=argparse.FileType('r'),
                        help=f"Path to json configuration {argparse_default}",
                        )
    #
    parser.add_argument("--show_map_at_each_round",
                        action="store_true", default=False,
                        help="Debug - Show map at each round (trashes & bot positions)")
    #
    parser.add_argument("-v", "--verbose",
                        action="store_true", default=False,
                        help="increase output verbosity (enable 'DEBUG' level log)")

    return parser


def parse_arguments(args=None):
    """
    Returns:
        # argparse.Namespace:
    """
    # return parsing
    return build_parser().parse_args(args)


def get_package_version(dist='forcity-trasherbot') -> str:
    """

    :param dist:
    """
    return pkg_resources.get_distribution(dist).version


def main(args=None):
    # Deal with inputs (stdin, parameters, etc ...)
    args = parse_arguments(args)

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=(logging.DEBUG if args.verbose else logging.INFO)
    )

    logger.info("application version: {}".format(get_package_version()))

    # Process simulation and get the result
    result_of_simulation = process(args)    # type: int

    # Deal with outputs
    return_result(result_of_simulation)


if __name__ == '__main__':
    main()
    sys.exit(0)
