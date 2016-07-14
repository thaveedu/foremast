"""CLI entry point for DNS cleanup."""
import argparse
import logging

from ...args import add_app, add_debug, add_env
from ...consts import LOGGING_FORMAT
from .destroy_dns import destroy_dns


def main():
    """Destroy any DNS related resources of an application

    Records in any Hosted Zone for an Environment will be deleted.
    """
    logging.basicConfig(format=LOGGING_FORMAT)

    parser = argparse.ArgumentParser(description=main.__doc__)
    add_debug(parser)
    add_app(parser)
    add_env(parser)
    args = parser.parse_args()

    logging.getLogger(__package__.split('.')[0]).setLevel(args.debug)

    assert destroy_dns(**vars(args))


if __name__ == '__main__':
    main()
