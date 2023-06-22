def raise_out_of_boundary_exception(
        index: int,
        minimum: int,
        maximum: int
) -> None:
    if not (
        (minimum <= index)
        and
        (index <= maximum)
    ):
        raise Exception(
            'out of boundary exception - the given value is outside the functions boundary'
        )
