from HardenedSteel.globals                          \
    import                                          \
    get_minimum_size_of_integer,                    \
    get_maximum_size_of_integer,                    \
    get_zero,                                       \
    get_maximum_size_of_unsigned_integer,           \
    get_system_random


def generate_unsigned_integer(
        begin: int = get_zero(),
        end: int = get_maximum_size_of_unsigned_integer()
) -> int:
    return get_system_random().randint(
        begin,
        end
    )


def generate_signed_integer(
        begin: int = get_minimum_size_of_integer(),
        end: int = get_maximum_size_of_integer()
) -> int:
    return get_system_random().randint(
        begin,
        end
    )
