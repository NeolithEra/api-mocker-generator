from __future__ import print_function

import argparse

from .logger import *
from .orchestra import play

__version__ = '0.0.1'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--swagger",
        required=True,
        help="Location of swagger document. Could be HTTP endpoint or local file system",
    )
    parser.add_argument("--verbose", action="store_true", default=False)
    return parser.parse_args()


def main():
    args = parse_args()

    if args.verbose:
        set_verbose_logging()
    else:
        logging.basicConfig(level=logging.INFO)

    info("Api-Mocker-Generator version {}".format(__version__))
    play(args.swagger)
