"""kmeow"""
from importlib import metadata

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # metadata package is not installed
    __version__ = "0.0.1"
