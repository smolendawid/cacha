"""The main functionality of cache-manager."""

# import hashlib
import logging
import os
import typing as t
import pathlib

import cacha.store.pickledb_store
import cacha.store.store_interface

LOGGER = logging.getLogger(__name__)

HOME = str(pathlib.Path.home())


def _compute_hash(argument: t.Any = None):
    """Compute hash from the Python object argument.

    In order to hash the object in Python, it has to implement
    the `__hash__()` function. It is not the case
    """
    return hash(argument)


def concatenate_arguments(args):
    return (_compute_hash(argument=arg) for arg in args)


def configure_cache(
    cache_root: str = HOME, cache_dir_name: str = ".cache_manager"
) -> cacha.store.store_interface.KeyValueStore:
    store = cacha.store.pickledb_store.PickleDbStore(
        cache_root=cache_root,
        cache_dir_name=cache_dir_name,
        db_file_name="store.json",
    )
    return store


def cache(
    func: t.Callable, args: t.Any = None, kwargs: t.Any = None, key: str = None
) -> t.Any:
    """Cache the resutls."""
    if kwargs is None:
        kwargs = {}

    store = configure_cache()

    if key is None:
        all_hashed_args = ()
        all_hashed_args += concatenate_arguments(args)
        all_hashed_args += concatenate_arguments(kwargs)
        key = "_".join(all_hashed_args)

    else:
        LOGGER.info("Caching based key: %s, because key was provided.")

    cache = store.get(concatenated_hash)
    if cache is None:
        result = func(*args, **kwargs)
        path = save_result()
        store.set(concatenated_hash, path)
    else:
        result = load_from_cache(concatenated_hash)

    return result
