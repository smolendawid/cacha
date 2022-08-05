"""The main functionality of cache-manager."""

# import hashlib
# import contextlib
import pathlib


HOME = str(pathlib.Path.home())


def cache(func, args: tuple = None, kwargs: dict = None):
    """Cache the resutls."""
    if kwargs is None:
        kwargs = {}
    return func(*args, **kwargs)
