from HardenedSteel.facades.texts.characters                                 \
    import                                                                  \
    random_lowercase_letter,                                                \
    random_uppercase_letter,                                                \
    random_letter

from HardenedSteel.facades.texts.exceptions                                 \
    import raise_out_of_boundary_exception

from HardenedSteel.globals                                                  \
    import                                                                  \
    get_maximum_size_of_integer,                                            \
    get_zero


def detect_outside_boundary_exception(
        index: int
):
    raise_out_of_boundary_exception(
        index,
        get_zero(),
        get_maximum_size_of_integer()
    )


def generate_lowercase_label_by_size(
        length_of_label: int
) -> str:
    detect_outside_boundary_exception(
        length_of_label
    )
    r_value: str = ''

    for position                                                            \
            in range(length_of_label):

        r_value = r_value + random_lowercase_letter()

    return r_value


def generate_uppercase_label_by_size(
        length_of_label: int
) -> str:
    detect_outside_boundary_exception(
        length_of_label
    )
    r_value: str = ''

    for position                                                            \
            in range(length_of_label):

        r_value = r_value + random_uppercase_letter()

    return r_value


def generate_label_by_size(
        length_of_label: int
) -> str:
    detect_outside_boundary_exception(
        length_of_label
    )
    r_value: str = ''

    for position                                                            \
            in range(length_of_label):
        r_value = r_value + random_letter()

    return r_value














