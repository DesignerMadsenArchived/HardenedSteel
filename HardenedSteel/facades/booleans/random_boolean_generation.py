from HardenedSteel.facades \
    import generate_random_bit


def generate_random_boolean() -> bool:
    return bool(
        generate_random_bit()
    )
