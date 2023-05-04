from toolz import pluck

tuples = [(1, 2, 3) for _ in range(100000)]
less_tuples = [(1, 2, 3) for _ in range(100)]


def test_pluck():
    for _ in pluck(2, tuples):
        pass

    for _ in range(1000):
        tuple(pluck(2, less_tuples))
