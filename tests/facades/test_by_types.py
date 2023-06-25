from HardenedSteel          \
    import                  \
    is_instance_of_integer, \
    is_instance_of_float,   \
    is_instance_of_string


def test_is_integer() -> None:
    assert is_instance_of_integer(
        4
    )


def test_is_float() -> None:
    assert is_instance_of_float(
        4.0
    )


def test_is_string() -> None:
    assert is_instance_of_string(
        'hello, world'
    )
