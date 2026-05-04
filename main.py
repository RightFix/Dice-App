from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from random import randint


class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._update_canvas, size=self._update_canvas)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.6, 0.6, 0.6, 1)
            self.rrect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.6, 0.6, 0.6, 1)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[20])


class Screen1(Screen):
    pass


class Screen2(Screen):
    pass


class MainApp(App):
    ran = randint


MainApp().run()
