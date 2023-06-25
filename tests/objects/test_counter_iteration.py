from HardenedSteel \
    import CounterObject

from HardenedSteel.objects.counters.limit import Limit


def test_iteration() -> None:
    counter: CounterObject = CounterObject()
    max: int = 10

    for i in iter(counter):
        if i == max:
            break

    assert counter.get_value() == max


def test_iteration_with_limit() -> None:
    max_integer: int = 10

    counter: CounterObject = CounterObject(
        limit=Limit(max_integer)
    )

    for i in iter(counter):
        pass

    assert counter.get_value() == max_integer
