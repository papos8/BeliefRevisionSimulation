import imp
from operator import imod
from kivy.app import App
from kivy.uix.widget import Widget

class Field(Widget):
    pass

class Simulation(App):
    def build(self):
        return Field()

if __name__ == '__main__':
    Field().run()