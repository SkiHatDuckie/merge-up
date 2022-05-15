import pygame as py

from block import Block
from bluedoor import BlueDoor
from reddoor import RedDoor
from splitpowerup import SplitPowerUp
from spike import Spike
from wall import Wall
from color import PURPLE


class BlockMerge(Block):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image = py.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill(PURPLE)

        self.split_attempt = False
    
    def process_input(self, events, pressed_keys, pressed_mouse):
        if pressed_keys[py.K_RIGHT] or pressed_keys[py.K_d]:
            self.direction.x = 1
        elif pressed_keys[py.K_LEFT] or pressed_keys[py.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if (pressed_keys[py.K_UP] or pressed_keys[py.K_w]) and self.on_ground:
            self.jump()
    
    def horizontal_movement_collision(self, objs: list):
        self.rect.x += self.direction.x * self.speed
        for obj in objs:
            if obj.rect.colliderect(self.rect):
                if type(obj) == Wall or type(obj) == RedDoor or type(obj) == BlueDoor:
                    if self.direction.x < 0:
                        self.rect.left = obj.rect.right
                        self.on_left = True
                        self.current_x = self.rect.left
                    elif self.direction.x > 0:
                        self.rect.right = obj.rect.left
                        self.on_right = True
                        self.current_x = self.rect.right
                if type(obj) == SplitPowerUp:
                    self.split_attempt = True
                if type(obj) == Spike:
                    self.dead = True
            else:
                if type(obj) == SplitPowerUp:
                    self.split_attempt = False

        if self.on_left and (self.rect.left < self.current_x or self.direction.x >= 0):
            self.on_left = False
        if self.on_right and (self.rect.right > self.current_x or self.direction.x <= 0):
            self.on_right = False

    def vertical_movement_collision(self, objs: list):
        self.apply_gravity()
        for obj in objs:
            if obj.rect.colliderect(self.rect):
                if type(obj) == Wall or type(obj) == RedDoor or type(obj) == BlueDoor:
                    if self.direction.y > 0:
                        self.rect.bottom = obj.rect.top
                        self.direction.y = 0
                        self.on_ground = True
                    elif self.direction.y < 0:
                        self.rect.top = obj.rect.bottom
                        self.direction.y = 0
                        self.on_ceiling = True
                if type(obj) == SplitPowerUp:
                    self.split_attempt = True
            else:
                if type(obj) == SplitPowerUp:
                    self.split_attempt = False

        if self.on_ground and self.direction.y < 0 or self.direction.y > 1:
            self.on_ground = False
        if self.on_ceiling and self.direction.y > 0.1:
            self.on_ceiling = False
