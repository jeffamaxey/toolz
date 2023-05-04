from toolz import get

tuples = [(1, 2, 3) for _ in range(100000)]


def test_get():
    for tup in tuples:
        get([1, 2], tup)
