import pygame as py

from block import Block
from mergepowerup import MergePowerUp
from purpledoor import PurpleDoor
from reddoor import RedDoor
from spike import Spike
from wall import Wall
from color import BLUE


class Block2(Block):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image.fill(BLUE)

        self.merge_attempt = False
    
    def process_input(self, events, pressed_keys, pressed_mouse):
        if pressed_keys[py.K_d]:
            self.direction.x = 1
        if pressed_keys[py.K_a]:
            self.direction.x = -1
        if not pressed_keys[py.K_a] and not pressed_keys[py.K_d]:
            self.direction.x = 0

        if pressed_keys[py.K_w] and self.on_ground:
            self.jump()
    
    def horizontal_movement_collision(self, objs: list):
        self.rect.x += self.direction.x * self.speed
        for obj in objs:
            if obj.rect.colliderect(self.rect):
                if type(obj) == Wall or type(obj) == PurpleDoor or type(obj) == RedDoor:
                    if self.direction.x < 0:
                        self.rect.left = obj.rect.right
                        self.on_left = True
                        self.current_x = self.rect.left
                    elif self.direction.x > 0:
                        self.rect.right = obj.rect.left
                        self.on_right = True
                        self.current_x = self.rect.right
                if type(obj) == MergePowerUp:
                    self.merge_attempt = True
                if type(obj) == Spike:
                    self.dead = True
            else:
                if type(obj) == MergePowerUp:
                    self.merge_attempt = False

        if self.on_left and (self.rect.left < self.current_x or self.direction.x >= 0):
            self.on_left = False
        if self.on_right and (self.rect.right > self.current_x or self.direction.x <= 0):
            self.on_right = False

    def vertical_movement_collision(self, objs: list):
        self.apply_gravity()
        for obj in objs:
            if obj.rect.colliderect(self.rect):
                if type(obj) == Wall or type(obj) == PurpleDoor or type(obj) == RedDoor:
                    if self.direction.y > 0:
                        self.rect.bottom = obj.rect.top
                        self.direction.y = 0
                        self.on_ground = True
                    elif self.direction.y < 0:
                        self.rect.top = obj.rect.bottom
                        self.direction.y = 0
                        self.on_ceiling = True
                if type(obj) == MergePowerUp:
                    self.merge_attempt = True
                if type(obj) == Spike:
                    self.dead = True
            else:
                if type(obj) == MergePowerUp:
                    self.merge_attempt = False

        if self.on_ground and self.direction.y < 0 or self.direction.y > 1:
            self.on_ground = False
        if self.on_ceiling and self.direction.y > 0.1:
            self.on_ceiling = False
