from typing import TypeVar, Generic

T = TypeVar('T')


class Nullable(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def __getattr__(self, item):
        try:
            return Nullable(self.value.item)
        except AttributeError:
            return Nullable(None)

    def __getitem__(self, item):
        try:
            return Nullable(self.value[item])
        except (TypeError, KeyError):
            return Nullable(None)

    def get(self) -> T | None:
        return self.value
