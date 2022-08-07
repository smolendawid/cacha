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

from cacha.version import __version__  # pylint: disable=unused-import

import cacha.manager
import cacha.logging_utils

cacha.logging_utils.configure_loggers(root_module_name=__name__)

cache = cacha.manager.cache
