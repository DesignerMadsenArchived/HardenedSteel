from HardenedSteel \
    import CounterObject


def test_iteration() -> None:
    counter: CounterObject = CounterObject()

    for i in iter(counter):
        print(counter.get_value())

        if i == 10:
            break

    assert counter.get_value() == 10
