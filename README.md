## Cache Manager

The simplest Python cache for Data Scientists

## Example

If you don't want to wait for a given `compute()` function to complete
each time you run the script, you can use context manager to cache the
output based on input parameters.

```python
import cache_manager as cm

with cm.cache():
    result = compute(data)

```

The cached data is stored in `$HOME/.cache_manager/`. Based on the argument
values,

## FAQ

**How is it different from _cachetools_?**

_cachetools_ supplies functional programming-style tools for in-memory
caching. _cache-manager_ allows you to cache the output of a function on
a local disk and load the results between runs. That's why it's suitable
for Data Scientist work.

**How can I clear the cache?**

Just delete the `$HOME/.cache_manager/` directory.
