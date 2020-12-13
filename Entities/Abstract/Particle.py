from abc import ABC
from Vector import Vector


class Particle(ABC):
    def __init__(self, mass=1, pos: Vector = Vector(0, 0, 0)):
        self.pos = pos
        self.mass = mass

    def move(self, v: Vector = Vector(0, 0, 0), t: float = 0) -> Vector:
        space_moved = v * t
        print(self.pos, v, space_moved)
        self.pos += space_moved
        print(self.pos)
        return self.pos

    def __repr__(self):
        return f"Particle(mass={self.mass}, pos={self.pos})"


if __name__ == "__main__":
    p, q = Particle(), Particle(pos=Vector(1, 2, 3))
    p.move(v=Vector(1, 2, 3), t=1)
    print(p)
