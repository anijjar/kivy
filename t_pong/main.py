"""
Synopsys: this script runs the kivy tutorial pong game
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    """ Widget defines the pong paddle """
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
        

class PongBall(Widget):
    """ Widget defines the pong ball """
    # velocity of ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # ReferenceListProperty allows shorthands
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """ Animate the sprite """
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    """ Widget defines the pong game """
    ball = ObjectProperty(None)
    p1 = ObjectProperty(None)
    p2 = ObjectProperty(None)

    def serve_ball(self, vel=(4,0)):
        """ Serve the ball """
        self.ball.center = self.center
        self.ball.velocity = vel

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.p1.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.p2.center_y = touch.y

    def update(self, dt):
        """ Update frame """
        self.ball.move()

        # bounce off paddles
        self.p1.bounce_ball(self.ball)
        self.p2.bounce_ball(self.ball)
        
        # bounce on top/bottom
        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # score a point?
        if self.ball.x < self.x:
            self.p2.score += 1
            self.serve_ball(vel=(4,0))
        if self.ball.right > self.width:
            self.p1.score += 1
            self.serve_ball(vel=(-4,0))


class PongApp(App):
    """ Parent class to enter game """
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()