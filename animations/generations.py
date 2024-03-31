from manim import *
import numpy as np
from statistics import mean
from constants import *


class GenerationsAnimation(Scene):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def construct(self):
        rows = []
        row_labels = []
        print(self.data)
        for i in range(len(self.data)):
            generation_data = self.data[i]
            generation_fitness_sum = sum(generation_data[1])
            generation_fitness_average = mean(generation_data[1])
            generation_maximum_x = generation_data[0][0]
            generation_maximum_y = generation_data[1][0]
            rows.append(
                [
                    str(i + 1),
                    str(generation_fitness_sum),
                    str(generation_fitness_average),
                    str(generation_maximum_y),
                ]
            )
            row_labels.append(i)

        table = Table(
            rows,
            col_labels=[
                Text("Generation"),
                Text("Sum"),
                Text("Average"),
                Text("Maximum"),
            ],
            include_outer_lines=True,
        ).set_column_colors(RED, GREEN, PURPLE, BLUE)
        table = table.scale(0.5)
        self.play(Write(Tex("Fitness Statistics by Generation").to_edge(edge=UP)))
        self.play(Write(table))
        self.wait(2)


def play_animation(data):
    animation = GenerationsAnimation(data)
    animation.render()
