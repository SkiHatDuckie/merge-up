from gameobject import GameObject
from color import LIGHTORANGE


class SplitPowerUp(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image.fill(LIGHTORANGE)
