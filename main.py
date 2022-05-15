import pygame as py
import pygame.freetype as py_freetype
from levelscene import LevelScene


def main(width, height, fps):
    py.init()
    py_freetype.init()
    screen = py.display.set_mode((width, height))
    py.display.set_caption("MergeUp!")
    clock = py.time.Clock()

    level_num = 0
    scene_ids = {
        0: LevelScene,
    }
    curr_scene_id = 0
    active_scene = LevelScene("levels\\level_" + str(level_num) + ".csv")

    while True:
        pressed_keys = py.key.get_pressed()
        pressed_mouse = py.mouse.get_pressed(3)

        # Event filtering
        filtered_events = []
        for event in py.event.get():
            quit_attempt = False

            if event.type == py.QUIT:
                quit_attempt = True
            elif event.type == py.KEYDOWN:
                alt_pressed = pressed_keys[py.K_LALT] or \
                              pressed_keys[py.K_RALT]
                if event.key == py.K_ESCAPE:
                    quit_attempt = True
                elif event.key == py.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
                break
            else:
                filtered_events.append(event)

        active_scene.processInput(filtered_events, pressed_keys, pressed_mouse)
        active_scene.update()
        active_scene.render(screen)

        # Check if request for scene switch has occured
        if active_scene.next != -1:
            if active_scene.next == 0 and curr_scene_id == 0:
                curr_scene_id == 0
                level_num += 0
                active_scene = LevelScene("levels\\level_" + str(level_num) + ".csv")
            elif active_scene.next == None:
                break
            else:
                curr_scene_id == active_scene.next
                active_scene = scene_ids[active_scene.next]()

        py.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main(704, 704, 60)
