from manim import *


class FunctionAnimation(Scene):
    def construct(self):
        axes = Axes(y_range=[0, 8, 1])
        axes.add_coordinates()
        self.play(Write(axes))
        self.wait(0.5)
        graph = axes.plot(lambda x: 4 * x**4 + 3 * x**3 + 2 * x**2 + x + 1, color=RED)
        self.play(Write(graph))
        self.wait(5)
