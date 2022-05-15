import pygame as py
from pathlib import Path

from block1 import Block1
from block2 import Block2
from blockmerge import BlockMerge
from bluedoor import BlueDoor
from mergepowerup import MergePowerUp
from purpledoor import PurpleDoor
from reddoor import RedDoor
from spike import Spike
from splitpowerup import SplitPowerUp
from wall import Wall
from settings import TILE_SIZE

# Each object on the grid is represented as a character or multiple characters.
cell_type = {
    " ": None,
    "#": Wall,
    "1": Block1,
    "2": Block2,
    "M": MergePowerUp,
    "S": SplitPowerUp,
    "^": Spike,
    "R": RedDoor,
    "B": BlueDoor,
    "P": PurpleDoor
}


class Level:
    def __init__(self) -> None:
        '''Generates a new level as a grid of characters representing game objects.

        The purpose of the grid is to define the initial objects in the level.
        It should not be updated during play.'''
        self.grid = []

        self.objects = []

        # Block 1, block 2, merged block
        self.blocks = [None, None, None]

    def _create_sprites(self) -> None:
        '''Creates a new game object for every cell in `self.grid`.
        
        cells representing `NoneType`s are skipped.'''
        # Initialize all game objects like a man
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                cell = self.grid[col][row]
                if cell != " ":
                    if cell == "1":
                        self.blocks[0] = Block1(row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    elif cell == "2":
                        self.blocks[1] = Block2(row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    else:
                        self.objects.append(cell_type[cell](row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    def _reset(self) -> None:
        self.objects = []
        self.blocks = [None, None, None]
        self._create_sprites()
    
    def generateFromCsv(self, path: str) -> None:
        '''Generate level grid from a .csv file.'''
        level_file = Path(path)

        with level_file.open() as csv:
            while True:
                line = csv.readline()
                if not line: break

                row = line.split(",")
                # Remove newline escape key
                row = row[0:-1]
                
                self.grid.append([])
                for item in row:
                    self.grid[-1].append(item)

        self._create_sprites()

    def process_input(self, events, pressed_keys, pressed_mouse):
        for obj in self.objects:
            obj.process_input(events, pressed_keys, pressed_mouse)
        
        for block in self.blocks:
            if block:
                block.process_input(events, pressed_keys, pressed_mouse)
    
    def update(self):
        for obj in self.objects:
            obj.update()
        
        for block in self.blocks:
            if block:
                block.update()
                block.horizontal_movement_collision(self.objects)
                block.vertical_movement_collision(self.objects)
                if block.dead:
                    self._reset()

        if self.blocks[0]:
            if self.blocks[0].merge_attempt and self.blocks[1].merge_attempt:
                self.blocks[2] = BlockMerge(self.blocks[0].rect.x, self.blocks[0].rect.y, TILE_SIZE, TILE_SIZE)
                self.blocks[0] = None
                self.blocks[1] = None
        elif self.blocks[2].split_attempt:
            self.blocks[0] = Block1(self.blocks[2].rect.x, self.blocks[2].rect.y, TILE_SIZE, TILE_SIZE)
            self.blocks[1] = Block2(self.blocks[2].rect.x, self.blocks[2].rect.y, TILE_SIZE, TILE_SIZE)
            self.blocks[2] = None
    
    def render(self, screen):
        for obj in self.objects:
            obj.render(screen)

        for block in self.blocks:
            if block:
                block.render(screen)
