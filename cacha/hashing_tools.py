import hashlib
import json
import typing as t
import inspect

import pandas as pd


def _compute_hash(argument: t.Hashable) -> str:
    """Compute hash from the Python object argument."""
    argument = _make_hashable(argument)
    return str(hashlib.md5(json.dumps(argument).encode()).hexdigest())


def _make_hashable(arg: t.Any) -> t.Hashable:
    """Convert input argument to hashable type."""
    if isinstance(arg, pd.DataFrame):
        # TODO: check if it's faster to convert ot string or tuple
        return str(pd.util.hash_pandas_object(arg).values)
    if callable(arg):
        return inspect.getsource(arg)
    return arg


def hash_arguments(args) -> t.List[str]:
    """Compute hash for all the arguments passed to the module."""
    return [_compute_hash(arg) for arg in args]


def hash_callable(func):
    """Hash the callable."""
    if not callable(func):
        raise ValueError("Function argument has to be callable")
    return _compute_hash(inspect.getsource(func))
