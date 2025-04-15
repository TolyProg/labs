import apackage as p
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

class Lab13App(App):
    def shapeI_cb(self, value):
        print(value)
    #def cb(self, value):
    #    print('cb', value)
    #def __init__(self):
    #    self.shape.bind(cb)
    pass


if __name__ == '__main__':
    Lab13App().run()
