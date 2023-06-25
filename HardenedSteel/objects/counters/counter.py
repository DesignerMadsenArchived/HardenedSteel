#!/usr/bin/env python
from HardenedSteel.objects.counters     \
    import                              \
    get_integer_zero,                   \
    get_integer_one,                    \
    is_integer_zero,                    \
    is_instance_of_integer,             \
    Limit


class CounterObject:
    def __init__(
            self,
            start_value: int = get_integer_zero(),
            move_by: int = get_integer_one(),
            limit: Limit | None = None
    ):
        self.value: int = start_value
        self.move: int = move_by

        self.limit: Limit | None = limit
        self.incremental: bool = True

    def __del__(self):
        del             \
            self.value, \
            self.move,  \
            self.limit

    def is_incremental(self) -> bool:
        return self.incremental

    def set_is_incremental(
            self,
            value: bool
    ) -> None:
        self.incremental = value

    def __iter__(self) -> iter:
        self.reset()
        return self

    def step(self) -> int:
        if self.is_incremental():
            self.increment()
        else:
            self.decrement()

        return self.get_value()

    def __call_move__(self):
        if self.has_no_limit():
            self.step()
        else:
            if self.get_limit().is_within_range(
                self.get_value()
            ):
                self.step()
            else:
                raise StopIteration

        return self.get_value()

    def __next__(self) -> int:
        return self.__call_move__()

    def reset(self):
        self.set_value(
            get_integer_zero()
        )

    def previous(self) -> int:
        return self.project_decrement()

    def after(self) -> int:
        return self.project_increment()

    def project_increase(
            self,
            by_value: int
    ) -> int:
        return self.get_value() + by_value

    def project_increment(self) -> int:
        return self.project_increase(
            get_integer_one()
        )

    def project_decrease(
            self,
            by_value: int
    ) -> int:
        return self.get_value() - by_value

    def project_decrement(self) -> int:
        return self.project_decrease(
            get_integer_one()
        )

    def get_limit(self) -> Limit | None:
        return self.limit

    def set_limit(
            self,
            value: Limit | None
    ) -> None:
        self.limit = value

    def remove_limit(self):
        self.set_limit(
            None
        )

    def has_limit(self) -> bool:
        return not self.has_no_limit()

    def has_no_limit(self) -> bool:
        return self.limit is None

    def get_move_size(self) -> int:
        return self.move

    def set_move_size(
            self,
            value: int
    ) -> None:
        self.move = value

    def get_value(self) -> int:
        return self.value

    def set_value(
            self,
            value: int
    ) -> None:
        self.value = value

    def increase(
            self,
            by_size: int
    ) -> None:
        self.set_value(
            self.value
            +
            by_size
        )

    def increment(self):
        self.increase(
            self.get_move_size()
        )

    def decrease(
            self,
            by_size: int
    ) -> None:
        self.set_value(
            self.value
            -
            by_size
        )

    def decrement(self):
        self.decrease(
            self.get_move_size()
        )

    def is_zero(self) -> bool:
        return is_integer_zero(
            self.get_value()
        )

    def is_not_zero(self) -> bool:
        return not is_integer_zero(
            self.get_value()
        )

    def __str__(self) -> str:
        return str(
            self.get_value()
        )

    def __int__(self) -> int:
        return self.get_value()

    def __invert__(self):
        inverse_counter = CounterObject(
            start_value=-self.get_value(),
            move_by=-self.get_move_size()
        )

        return inverse_counter

    def __lt__(
            self,
            other
    ) -> bool:
        if is_instance_of_counter_object(
            other
        ):
            compare_to: CounterObject = other
            return self.get_value() < compare_to.get_value()
        
        if is_instance_of_integer(
            other
        ):
            compare_to: int = other
            return self.get_value() < compare_to

        return False

    def __gt__(
            self,
            other
    ) -> bool:
        if is_instance_of_counter_object(
            other
        ):
            compare_to: CounterObject = other
            return self.get_value() > compare_to.get_value()
        
        if is_instance_of_integer(
            other
        ):
            compare_to: int = other
            return self.get_value() > compare_to
        
        return False

    def __add__(
            self,
            other
    ):
        if is_instance_of_counter_object(
            other
        ):
            o_co: CounterObject = other
            self.increase(
                o_co.get_value()
            )

        if is_instance_of_integer(
            other
        ):
            o_int: int = other
            self.increase(
                o_int
            )

        return self

    def __sub__(
            self,
            other
    ):
        if is_instance_of_counter_object(
            other
        ):
            o_co: CounterObject = other
            self.decrease(
                o_co.get_value()
            )

        if is_instance_of_integer(
            other
        ):
            o_int: int = other

            self.decrease(
                o_int
            )

        return self

    def __eq__(
            self,
            other
    ) -> bool:
        r_val: bool = False

        if is_instance_of_counter_object(
                other
        ):
            o_co: CounterObject = other
            r_val = bool(
                self.get_value()
                ==
                o_co.get_value()
            )

            return r_val

        if is_instance_of_integer(
                other
        ):
            o_int: int = other
            r_val = bool(
                self.get_value()
                ==
                o_int
            )

            return r_val

        return r_val


def is_instance_of_counter_object(
        value
) -> bool:
    return isinstance(
        value,
        CounterObject
    )
