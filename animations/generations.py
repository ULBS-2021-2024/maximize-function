from manim import *


class GenerationsAnimation(Scene):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def construct(self):
        axes = Axes(y_range=[0, 8, 1])
        axes.add_coordinates()
        self.play(Write(axes))
        self.wait(0.5)
        graph = axes.plot(lambda x: x**2, color=RED)
        self.play(Write(graph))
        self.wait(5)


def play_animation(data):
    animation = GenerationsAnimation(data)
    animation.render()
