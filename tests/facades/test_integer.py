from tests.facades                                                                      \
    import                                                                              \
    generate_unsigned_integer,                                                          \
    generate_signed_integer,                                                            \
    get_integer_zero,                                                                           \
    get_maximum_size_of_unsigned_integer,                                               \
    get_minimum_size_of_integer,                                                        \
    get_maximum_size_of_integer


def test() -> None:
    print()
    assert True


def test_signed() -> None:
    example: int = generate_signed_integer()
    print('example-signed: ', example)

    assert                                                                              \
        (get_minimum_size_of_integer() <= example)                                      \
        and                                                                             \
        (example <= get_maximum_size_of_integer())


def test_unsigned() -> None:
    example: int = generate_unsigned_integer()
    print('example-unsigned: ', example)

    assert                                                                              \
        (get_integer_zero() <= example)                                                         \
        and                                                                             \
        (example <= get_maximum_size_of_unsigned_integer())
