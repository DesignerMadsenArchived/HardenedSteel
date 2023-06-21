from steel.globals.singletons.SingletonSystenRandom \
    import get_system_random


def character_in_range(
        begin: int,
        end: int
):
    random_number: int = get_system_random().randint(begin, end)
    return chr(random_number)


def random_letter() -> str:
    return character_in_range(97, 122)


def generate_label_by_size(
        length_of_label: int
) -> str:
    r_value: str = ''

    for position in range(length_of_label):
        r_value = r_value + random_letter()

    return r_value
