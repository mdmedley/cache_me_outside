try:
    from functools import lru_cache as cache_me_outside
except ImportError:
    from backports.functools_lru_cache import lru_cache as cache_me_outside
