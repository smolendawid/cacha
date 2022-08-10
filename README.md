## Cacha

The simplest Python cache for Data Scientist,

## Example

If you don't want to wait for a given `compute()` function to complete
each time you run the script, you can cache the output of the function

```python
import cacha

result = cacha.cache(compute, (data)):

```

The cached data is stored in `$HOME/.cacha/`. Each time you run the
function with identical input arguments, the output data will be loaded, not
computed.

It can be easily used with popular data structures as pandas DataFrame or
numpy array. In case of complicated python objects that can't be easily hasheed,
you can use additional `key` parameter that forces saving the cache based on
the `key` value.

## FAQ

**How is it different other caching packages?**

In contrary to many tools, cacha

- is used at the function call, not definition. Many packages the `@cache`
  decorator that has to be used before definition of a function that is
  not easy enough to use.
- it stores the cache on disk which means you can use cache between runs.
  This is convenient in data science work.

**How can I clear the cache?**

Just delete the `$HOME/.cacha/` directory. You can also call `cacha.clean()`
which has the same effect.
