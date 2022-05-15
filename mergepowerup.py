from gameobject import GameObject
from color import LIGHTYELLOW


class MergePowerUp(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image.fill(LIGHTYELLOW)
