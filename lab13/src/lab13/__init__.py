import apackage as p
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class Lab13App(App):
    def build(self):
        self.title = 'lab13: Gadostlivaya ZEST Bred Mk.II Deluxe Edition'
    def do(self, f):
        a = float(self.root.ids.a.text)
        b = float(self.root.ids.b.text)
        c = float(self.root.ids.c.text)
        m = str(self.root.ids.material.text)
        self.root.ids.out.text = p.select(self.root.ids.shape.text,a,b,c,m)
        p.selected.m = m
        if f == 'report':
            self.root.ids.out.text = p.report()
        else:
            self.root.ids.out.text = str(getattr(p.selected, f)())


if __name__ == '__main__':
    Lab13App().run()
