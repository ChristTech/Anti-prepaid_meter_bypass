import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (305, 480)


class AdminPageApp(MDApp):

    def build(self):
        global screen_manager
        # controls the separate screens
        screen_manager = ScreenManager( )
        # this loads the specified .kv file to be used compared to just returning it from the build file
        screen_manager.add_widget(Builder.load_file("admin.kv"))
        # screen_manager.add_widget(Builder.load_file("admin_login.kv"))
        return screen_manager


if __name__ == "__main__":
    app = AdminPageApp()
    app.run()