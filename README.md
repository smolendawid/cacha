## Cache Manager

The simplest Python cache for Data Scientists

## Example

If you don't want to wait for a given `compute()` function to complete
each time you run the script, you can cache the output of the function

```python
import cache_manager as cm

result = cm.cache(compute, (data)):

```

The cached data is stored in `$HOME/.cache_manager/`. Each time you run the
function with identical input arguments, the output data will be loaded, not
computed.

## FAQ

**How is it different from _cachetools_?**

_cachetools_ supplies functional programming-style tools for in-memory
caching. _cache-manager_ allows you to cache the output of a function on
a local disk and load the results between runs. That's why it's suitable
for Data Scientist work.

**How can I clear the cache?**

Just delete the `$HOME/.cache_manager/` directory.
