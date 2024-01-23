import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (305, 480)


class LoginApp(MDApp):

    def change_screen(self, name):
        # whatever argument will be passed in as name, it will change the screen
        screen_manager.current = name

    def build(self):
        global screen_manager
        # controls the separate screens
        screen_manager = ScreenManager()
        # this loads the specified .kv file to be used compared to just returning it from the build file
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("admin_login.kv"))
        return screen_manager

    def AdminLogin(self):
        # gets the name of the current screen i' working on
        current_screen = self.root.get_screen("LoginPage")
        current_screen.ids.slide.load_next(mode="next")

    def UserLogin(self):
        # gets the name of the current screen i' working on
        current_screen = self.root.get_screen("LoginPage")
        current_screen.ids.slide.load_previous()


    def anim(self, widget):
        anim = Animation(pos_hint = {"center_y": 1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint = {"center_y": .85})
        anim.start(widget)

    def icons(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"centre_y": .85})
        anim.start(widget)

    def text(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)


if __name__ == "__main__":
    app = LoginApp()
    app.run()

