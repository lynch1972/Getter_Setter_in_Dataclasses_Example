"""Points Module"""

from dataclasses import dataclass, field


@dataclass(order=True, slots=True)
class Point:
    """Point Class"""

    val_a: float = 0
    val_b: float = 0
    _x_val: float | None = field(init=False, repr=False, default=None)

    def __post_init__(self):
        """Post Initializer"""

    @property
    def start_x_val_value(self) -> float:
        """Starting Value to be assigned if desired"""
        return self.val_a + self.val_b

    @property
    def x_val(self) -> float:
        """x_val Getter Method"""
        print(f"Get x_val that previously was {self._x_val}")
        return self._x_val

    @x_val.setter
    def x_val(self, new_x: float) -> None:
        """x_val Setter Method"""
        print(f"Set x_val from {self._x_val} to {new_x}")
        self._x_val = new_x

    @x_val.deleter
    def x_val(self) -> None:
        """x_val Deleter Method"""
        print("Delete x_val")
        self._x_val = None
