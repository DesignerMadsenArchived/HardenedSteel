from steel.facades.texts.characters \
    import get_system_random


def random_uppercase_letter() -> str:
    return character_in_range(
        ord('A'),
        ord('Z')
    )


def random_lowercase_letter() -> str:
    return character_in_range(
        ord('a'),
        ord('z')
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
