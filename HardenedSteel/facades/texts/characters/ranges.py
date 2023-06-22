from HardenedSteel.facades.texts.characters \
    import                                  \
    get_system_random,                      \
    generate_random_boolean

ascii_lowercase_begin:  int = ord('a')
ascii_lowercase_end:    int = ord('z')

ascii_uppercase_begin:  int = ord('A')
ascii_uppercase_end:    int = ord('Z')


def random_letter() -> chr:
    choose_uppercase: bool = generate_random_boolean()

    if choose_uppercase:
        return random_uppercase_letter()
    else:
        return random_lowercase_letter()


def random_uppercase_letter() -> chr:
    global                          \
        ascii_uppercase_begin,      \
        ascii_uppercase_end

    return character_in_range(
        ascii_uppercase_begin,
        ascii_uppercase_end
    )


def random_lowercase_letter() -> chr:
    global                          \
        ascii_lowercase_begin,      \
        ascii_lowercase_end

    return character_in_range(
        ascii_lowercase_begin,
        ascii_lowercase_end
    )


def character_in_range(
        begin: int,
        end: int
) -> chr:
    random = get_system_random()

    random_number: int = random.randint(
        begin,
        end
    )

    return chr(
        random_number
    )
