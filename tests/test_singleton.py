from random \
    import SystemRandom

from HardenedSteel.globals \
    import \
    get_system_random, \
    set_system_random


def test_get() -> None:
    assert not (get_system_random() is None)


def test_set() -> None:
    set_system_random(
        SystemRandom()
    )

    assert not (get_system_random() is None)
