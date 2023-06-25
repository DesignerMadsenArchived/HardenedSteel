from HardenedSteel.globals                      \
    import                                      \
    get_system_random,                          \
    get_integer_one,                                    \
    get_conversion_of_a_byte_to_bits


def generate_random_bit() -> int:
    random = get_system_random()

    return random.getrandbits(
        get_integer_one()
    )


def generate_random_bits(
        by_size: int = get_conversion_of_a_byte_to_bits()
):
    random = get_system_random()

    return random.getrandbits(
        by_size
    )


def generate_random_bytes(
        size: int
) -> bytes:
    random = get_system_random()

    return random.randbytes(
        size
    )
