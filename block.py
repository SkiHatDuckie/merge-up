import pygame as py

from gameobject import GameObject
from spike import Spike
from wall import Wall


class Block(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.image = py.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))

        # Movement
        self.direction = py.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # Status
        self.status = 'idle'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.dead = False

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def horizontal_movement_collision(self, objs: list):
        self.rect.x += self.direction.x * self.speed
        for obj in objs:
            if obj.rect.colliderect(self.rect):
                if type(obj) == Wall:
                    if self.direction.x < 0:
                        self.rect.left = obj.rect.right
                        self.on_left = True
                        self.current_x = self.rect.left
                    elif self.direction.x > 0:
                        self.rect.right = obj.rect.left
                        self.on_right = True
                        self.current_x = self.rect.right
                if type(obj) == Spike:
                    self.dead = True

        if self.on_left and (self.rect.left < self.current_x or self.direction.x >= 0):
            self.on_left = False
        if self.on_right and (self.rect.right > self.current_x or self.direction.x <= 0):
            self.on_right = False

    def vertical_movement_collision(self, objs: list):
        self.apply_gravity()
        for obj in objs:
            if obj.rect.colliderect(self.rect):
                if type(obj) == Wall:
                    if self.direction.y > 0:
                        self.rect.bottom = obj.rect.top
                        self.direction.y = 0
                        self.on_ground = True
                    elif self.direction.y < 0:
                        self.rect.top = obj.rect.bottom
                        self.direction.y = 0
                        self.on_ceiling = True
                if type(obj) == Spike:
                    self.dead = True

        if self.on_ground and self.direction.y < 0 or self.direction.y > 1:
            self.on_ground = False
        if self.on_ceiling and self.direction.y > 0.1:
            self.on_ceiling = False

    def update(self):
        self.get_status()
