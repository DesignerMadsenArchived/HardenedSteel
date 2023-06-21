from sys \
    import maxsize

integer_max_size: int = maxsize
zero: int = 0


def get_maximum_size_of_integer() -> int:
    global integer_max_size
    return integer_max_size


def get_zero() -> int:
    global zero
    return zero
