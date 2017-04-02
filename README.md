[![PyPI](https://img.shields.io/pypi/v/cache_me_outside.svg?style=flat-square)](https://pypi.python.org/pypi/cache_me_outside) [![Travis](https://img.shields.io/travis/mdmedley/cache_me_outside.svg?style=flat-square)](https://travis-ci.org/mdmedley/cache_me_outside)

# Cache Me Outside
Cache me outside!

### Version
v0.1


### Installation
```sh
pip install cache_me_outside
```


### Quickstart
```python
from cache_me_outside import cache_me_outside

# Just decorate the function you want to implement a cache for and use just like lru_cache
@cache_me_outside(maxsize=20)
def some_expensive_io_function():
    return 'Some string'
```


### Development
Want to contribute? Great! Fork and submit a pull request!

### Alternatives
- [Python 2](https://github.com/jaraco/backports.functools_lru_cache)
- [Python 3](https://docs.python.org/3.4/library/functools.html#functools.lru_cache)
