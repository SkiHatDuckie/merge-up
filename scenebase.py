class SceneBase:
    def __init__(self):
        '''Interface for creating new game scenes.
        
        `id` is an integer used to identify the current scene.
        This enables the ability to switch to another scene, 
        without needing the other scene to be in the same file as the current one.'''
        self.next = -1

    def process_input(self, events, pressed_keys, pressed_mouse):
        print("oh noes!, you didn't override this in the child class")

    def update(self):
        print("oh noes!, you didn't override this in the child class")

    def render(self, screen):
        print("oh noes!, you didn't override this in the child class")

    def switchToScene(self, scene_id):
        self.next = scene_id

    def terminate(self):
        self.switchToScene(None)
        print("app terminated")