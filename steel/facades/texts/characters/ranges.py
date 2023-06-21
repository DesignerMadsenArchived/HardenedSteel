from steel.facades.texts.characters \
    import get_system_random


def random_lowercase_letter() -> str:
    return character_in_range(
        97,
        122
    )


def character_in_range(
        begin: int,
        end: int
):
    random = get_system_random()

    random_number: int = random.randint(
        begin,
        end
    )

    return chr(
        random_number
    )
