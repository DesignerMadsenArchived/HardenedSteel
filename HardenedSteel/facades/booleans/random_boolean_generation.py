from HardenedSteel.facades.booleans                 \
    import                                          \
    get_system_random,                              \
    get_one


def generate_random_boolean() -> bool:
    random = get_system_random()
    
    return bool(
        random.getrandbits(
            get_one()
        )
    )
