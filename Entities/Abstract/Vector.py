class Vector:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        return Vector(
            x=self._x + other._x,
            y=self._y + other._y,
            z=self._z + other._z,
        )

    def __mul__(self, other):
        t = type(other)
        if t is int or t is float:
            return Vector(
                x=self._x * other,
                y=self._y * other,
                z=self._z * other,
            )

    def __repr__(self):
        return f"Vector({self._x}, {self._y}, {self._z})"


if __name__ == "__main__":
    pos = Vector(1, 2, 3)
    print("Normal Vector", pos)

    other_add = Vector(3, 2, 1)
    print(f"Sum of: {pos} + {other_add} =", pos + other_add)

    other_int_mul = 1.234
    print(f"Real mult: {pos} * {other_int_mul} =", pos * other_int_mul)
