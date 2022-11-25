"""Points Module"""

from dataclasses import dataclass, field


@dataclass(order=True, slots=True)
class Point:
    """Point Class"""
    a: float = 0
    b: float = 0
    _x: float | None = field(init=False, repr=False, default=None)

    def __post_init__(self):
        """Post Initializer"""

    @property
    def start_x_value(self) -> float:
        return self.a + self.b

    @property
    def x(self) -> float:
        print(f"Get x that previously was {self._x}")
        return self._x

    @x.setter
    def x(self, new_x: float) -> None:
        print(f"Set x from {self._x} to {new_x}")
        self._x = new_x

    @x.deleter
    def x(self) -> None:
        print("Delete X")
        self._x = None

