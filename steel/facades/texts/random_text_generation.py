from steel.facades.texts.characters \
    import random_lowercase_letter


def generate_label_by_size(
        length_of_label: int
) -> str:
    r_value: str = ''

    for position \
        in range(
            length_of_label
        ):
        r_value = r_value + random_lowercase_letter()

    return r_value

















