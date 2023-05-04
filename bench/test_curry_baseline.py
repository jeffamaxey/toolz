from toolz import get
from functools import partial


pairs = [(1, 2) for _ in range(100000)]


def test_get():
    first = partial(get, 0)
    for p in pairs:
        first(p)
