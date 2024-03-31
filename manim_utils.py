from constants import *
from animations.generations import *

data = []


def add_generation_data(decoded_values, fitness_values, generation):
    data.append(tuple((decoded_values, fitness_values, generation)))


def generate_animation():
    play_animation(data)
