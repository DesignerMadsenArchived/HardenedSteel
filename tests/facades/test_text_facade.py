from steel.facades.texts \
    import generate_label_by_size


def test_generate_label() -> None:
    size: int = 20

    r_tex: str = generate_label_by_size(size)
    print('result: ', r_tex)

    assert len(r_tex) == size
