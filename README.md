## In development

This is expected to be in development Q3 2022. Please do not rely on this
software before the official release.

## Cacha

The simplest Python cache for Data Scientist:

- cache on disk, use between runs,
- use at function call, not definition.

## Example

If you don't want to wait for a given `compute()` function to complete
each time you run the script, you can cache it:

```python
import cacha

result = compute(data) # regular usage, slow

result = cacha.cache(compute, (data, ))  # usage with cache

```

The cached data is stored in `$HOME/.cacha/`. Each time you run the
function with identical input arguments, the output data will be loaded,
instead of being computed.

It can be easily used with popular data structures like `pandas.DataFrame` or
`numpy.array`. In case of complicated python objects that can't be easily
hashed, you can use additional `key` parameter that forces saving the cache
based on the `key` value.

```python
import cacha

result = cacha.cache(compute, (data, ), key="compute-v3")

```

## FAQ

**How is it different other caching packages?**

In contrary to many other tools, _cacha_:

- is used at the function call, not definition. Many packages implement
  the `@cache` decorator that has to be used before definition of
  a function that is not easy enough to use.
- it stores the cache on disk which means you can use cache between runs.
  This is convenient in data science work.

**How can I clear the cache?**

Just delete the `$HOME/.cacha/` directory. You can also call `cacha.clean()`
which has the same effect.

**Why does it requre the pandas, numpy and other libraries?**
In order to properly cache the objects from the specific packages, it is
required to have the access to the functions they provide in that purpose.
The main goal of cache is not to be lightweight but to provide the best
developer experience.

However most of the required packages are usually
used in Machine Learning projects anyway.
