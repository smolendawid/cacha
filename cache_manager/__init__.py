"""
The cache_manager module provides the main functionality of the package.

The provided API helps managing the cache easily.
For example:

.. code:: python

    import cache_manager as cm

    data
    with cm.cache():
        function

"""

from cache_manager.version import __version__  # pylint: disable=unused-import

import cache_manager.manager


cache = cache_manager.manager.cache
