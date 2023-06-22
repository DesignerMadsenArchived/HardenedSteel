from random                                             \
    import SystemRandom

singleton_system_random: SystemRandom | None = None


def get_system_random() -> SystemRandom:
    global singleton_system_random

    if is_system_random_none():
        set_system_random(
            SystemRandom()
        )

    return singleton_system_random


def set_system_random(
        value: SystemRandom
) -> None:
    global singleton_system_random
    singleton_system_random = value


def is_system_random_none() -> bool:
    global singleton_system_random
    return singleton_system_random is None
