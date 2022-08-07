"""Implementation of `cacha.store.store_interface` and pickledb."""

import os
import pickledb
import cacha.store.store_interface


class PickleDbStore(cacha.store.store_interface.KeyValueStore):
    """See base class."""

    def __init__(
        self, cache_root: str, cache_dir_name: str, db_file_name: str
    ) -> None:
        """Create the store object.

        Args:
            cache_root: path to cache root
            cache_dir_name: name of cache directory
            db_file_name: name of cache file
        """
        super().__init__()
        os.makedirs(os.path.join(cache_root, cache_dir_name))
        self.db_path = os.path.join(cache_root, cache_dir_name, db_file_name)
        self.db = pickledb.load(
            self.db_path,
            False,
        )  # pylint: disable=invalid-name

    def set(self, key, value):
        """See base class."""
        self.db.set(key, value)

    def get(self, key):
        """See base class."""
        self.db.get(key)
