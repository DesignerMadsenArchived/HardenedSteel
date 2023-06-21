from steel.facades.texts.characters \
    import \
    random_lowercase_letter, \
    random_uppercase_letter


def generate_label_by_size(
        length_of_label: int
) -> str:
    r_value: str = ''

    for position \
            in range(length_of_label):

        r_value = r_value + random_lowercase_letter()

    return r_value


def generate_uppercase_label_by_size(
        length_of_label: int
) -> str:
    r_value: str = ''

    for position \
            in range(length_of_label):

        r_value = r_value + random_uppercase_letter()

    return r_value

















