from tests.facades \
    import generate_random_boolean


def default_test() -> None:
    assert True


def test_random_boolean() -> None:
    result: bool = generate_random_boolean()
    print('random boolean: ', str(result))
    assert isinstance(result, bool)
