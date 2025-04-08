from kivy.app import App
from kivy.uix.widget import Widget


class UI(Widget):
    pass


class Lab13App(App):
    def build(self):
        return UI()


if __name__ == '__main__':
    Lab13App().run()
