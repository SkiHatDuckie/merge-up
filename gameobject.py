import pygame as py


class GameObject(py.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        '''Interface for creating new game objects.'''
        super().__init__()
        self.image = py.Surface((width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
    
    def process_input(self, events, pressed_keys, pressed_mouse):
        pass

    def update(self):
        pass
    
    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
