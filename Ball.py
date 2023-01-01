from operator import imod
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from random import randint


class Ball(kuix.Widget):
    velocity_x = kpro.NumericProperty(0)
    velocity_y = kpro.NumericProperty(0)

    ball_velocity = kpro.ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = kvec.Vector(*self.ball_velocity) + self.pos
