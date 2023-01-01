
from operator import imod
from kivy.app import App
import kivy.uix.widget as kuix
import kivy.properties as kpro
import kivy.vector as kvec
import kivy.clock as kclo
from random import randint
import kivy.lang.builder as kbui
import Agent
import Ball


class Field(kuix.Widget):
    ball = kpro.ObjectProperty(None)
    # agent = kpro.ObjectProperty(None)

    # Initial values for the ball
    def start_ball(self):
        self.ball.center = self.center
        self.ball.velocity = kvec.Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # Bounce on top or bottom
        # TODO: Restart game
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Bounce left or right
        # TODO: Restart game
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class Simulation(App):
    def build(self):
        new_field = Field()
        new_field.start_ball()
        kclo.Clock.schedule_interval(new_field.update, 1.0/60.0)
        return kbui.Builder.load_file('simulation.kv')


if __name__ == '__main__':
    Simulation().run()
