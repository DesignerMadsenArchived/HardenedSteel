from HardenedSteel.globals \
    import get_integer_zero


def is_integer_zero(
        value: int
) -> bool:
    return get_integer_zero() == value
