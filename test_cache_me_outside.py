from random import randint

import cache_me_outside


@cache_me_outside()
def foo():
    return randint()


def test_execution():
    """Validates cache works as expected"""
    assert foo() == foo()
