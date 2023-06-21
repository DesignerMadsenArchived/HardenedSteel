from tests.facades                      \
    import                              \
    generate_lowercase_label_by_size,   \
    generate_uppercase_label_by_size,   \
    generate_label_by_size


def test() -> None:
    print()
    assert True


def test_lowercase_generate_label() -> None:
    size: int = 20

    r_tex: str = generate_lowercase_label_by_size(size)
    print('result-lowercase: ', r_tex)

    assert len(r_tex) == size


def test_generate_label_uppercase() -> None:
    size: int = 20

    r_tex: str = generate_uppercase_label_by_size(size)
    print('result-uppercase: ', r_tex)

    assert len(r_tex) == size


def test_generate_label() -> None:
    size: int = 20

    r_tex: str = generate_label_by_size(size)
    print('result_label: ', r_tex)

    assert len(r_tex) == size
