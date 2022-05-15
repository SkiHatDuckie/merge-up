from gameobject import GameObject
from color import LIGHTPURPLE


class PurpleDoor(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image.fill(LIGHTPURPLE)