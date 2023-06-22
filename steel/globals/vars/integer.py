from sys \
    import maxsize

unsigned_max_size: int = 4294967295

integer_max_size: int = maxsize
integer_min_size: int = -maxsize - 1

zero: int = 0


def get_maximum_size_of_unsigned_integer() -> int:
    global unsigned_max_size
    return unsigned_max_size


def get_minimum_size_of_integer() -> int:
    global integer_min_size
    return integer_min_size


def get_maximum_size_of_integer() -> int:
    global integer_max_size
    return integer_max_size


def get_zero() -> int:
    global zero
    return zero
