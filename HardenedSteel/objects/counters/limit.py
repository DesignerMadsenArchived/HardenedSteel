class Limit:
    def __init__(
            self,
            limit_value: int
    ):
        self.value: int = limit_value
        self.in_reverse: bool = False

    def __del__(self):
        del self.value

    def is_within_range(
            self,
            position: int
    ) -> bool:
        if self.is_in_reverse():
            return position > self.get_value()
        else:
            return position < self.get_value()

    def is_in_reverse(self) -> bool:
        return self.in_reverse

    def set_is_in_reverse(
            self,
            value: bool
    ) -> None:
        self.in_reverse = value

    def get_value(self) -> int:
        return self.value

    def set_value(
            self,
            to: int
    ) -> None:
        self.value = to

    def __int__(self) -> int:
        return self.get_value()
