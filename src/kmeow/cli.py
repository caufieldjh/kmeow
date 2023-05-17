"""CLI for kmeow"""

import click
import logging

from kmeow import __version__
from kmeow.utils import store_api_key

@click.group()
@click.option("-v", "--verbose")
@click.version_option(__version__)
def main(verbose: bool):
    """CLI for kmeow.

    :param verbose: bool, verbose output if used.
    """
    logger = logging.getLogger()
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    logger.info(f"Logger {logger.name} set to level {logger.level}")

@click.argument("input", required=True)
def store_key(api_key: str):
    """Utility for storing OpenAI API key."""
    store_api_key(api_key)
