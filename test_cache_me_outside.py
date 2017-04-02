from random import random

from cache_me_outside import cache_me_outside


@cache_me_outside()
def foo():
    return random()


def test_execution():
    """Validates cache works as expected"""
    assert foo() == foo()
