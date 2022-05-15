import pygame.freetype as py_freetype

from scenebase import SceneBase
from level import Level
from color import WHITE, GRAY


# Scene designed to load and work with any level
class LevelScene(SceneBase):
    def __init__(self, level_path: str):
        '''Scene designed to load and work with any level.
        
        `level_path` is the path to the level .csv file to load
        '''
        SceneBase.__init__(self)

        self.level = Level()
        self.level.generateFromCsv(level_path)

        font_vt323_24 = py_freetype.Font("assets\\fonts\\VT323-Regular.ttf", 24)
        self.level_title = font_vt323_24.render(level_path[6:-4], fgcolor=GRAY)
        

    def processInput(self, events, pressed_keys, pressed_mouse):
        self.level.process_input(events, pressed_keys, pressed_mouse)

    def update(self):
        self.level.update()

    def render(self, screen):
        screen.fill(WHITE)
        self.level.render(screen)
        screen.blit(self.level_title[0], (10, 10))
