
from operator import imod
from kivy.app import App
import kivy.uix.widget as kuix

class Field(kuix.Widget):
    pass

class Simulation(App):
    def build(self):
        return Field()

if __name__ == '__main__':
    Simulation().run()