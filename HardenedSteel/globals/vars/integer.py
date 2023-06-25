from HardenedSteel.globals.vars \
    import maxsize

zero: int = 0
one: int = 1
two: int = 2
three: int = 3
four: int = 4
five: int = 5
six: int = 6
seven: int = 7
eight: int = 8
nine: int = 9

unsigned_max_size: int = 4294967295

integer_max_size: int = maxsize
integer_min_size: int = -maxsize - one


def get_maximum_size_of_unsigned_integer() -> int:
    global unsigned_max_size
    return unsigned_max_size


def get_minimum_size_of_integer() -> int:
    global integer_min_size
    return integer_min_size


def get_maximum_size_of_integer() -> int:
    global integer_max_size
    return integer_max_size


def get_integer_zero() -> int:
    global zero
    return zero


def get_integer_one() -> int:
    global one
    return one
