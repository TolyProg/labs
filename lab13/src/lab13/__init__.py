import apackage as p
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class Lab13App(App):
    def build(self):
        self.title = 'lab13: Gadostlivaya ZEST Bred Mk.II Deluxe Edition'
    def test_cb(self):
        print('test_cb()')




if __name__ == '__main__':
    Lab13App().run()
