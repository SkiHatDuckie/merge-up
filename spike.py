import pygame as py

from gameobject import GameObject
from color import WHITE, LIGHTGRAY


class Spike(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image.fill(WHITE)
    
    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        py.draw.polygon(
            screen, 
            LIGHTGRAY, 
            (
                (self.rect.x + self.rect.width / 2, self.rect.y),
                (self.rect.x, self.rect.y + self.rect.height),
                (self.rect.x + self.rect.width, + self.rect.y + self.rect.height)
            )
        )
