import random
from constants import *
from statistics import mean


def compute_actual_count(fitness, probability):
    actual_count = [0] * len(probability)
    number_of_spins = 100

    for _ in range(number_of_spins):
        spin_result = random.random()
        cumulative_prob = 0
        for i, prob in enumerate(probability):
            cumulative_prob += prob
            if spin_result <= cumulative_prob:
                actual_count[i] += 1
                break
    return actual_count


def compute_expected_count(fitness):
    average_fitness = mean(fitness)
    expected_count = []
    for i in range(len(fitness)):
        expected_count.append(fitness[i] / average_fitness)
    return expected_count


def compute_probability_of_selection(fitness):
    fitness_sum = sum(fitness)
    probability = []
    for i in range(len(fitness)):
        probability.append(fitness[i] / fitness_sum)
    return probability


def evaluate_function(x):
    return 4 * x**4 + 3 * x**3 + 2 * x**2 + x + 1


def compute_fitness(values):
    fitness = []
    for i in range(len(values)):
        fitness.append(evaluate_function(values[i]))
    return fitness


def binary_decode(binary_string, a, b):
    n = 10
    decoded_number = int(binary_string, 2)
    decoded_number = decoded_number / (2**n - 1) * (b - a) + a
    return decoded_number


def binary_encode(x, a, b):
    n = 10
    corresponding_integer = int((x - a) / (b - a) * (2**n - 1))
    return bin(corresponding_integer)[2:].zfill(n)


def select_initial_population(a, b, N):
    initial_population = []
    for i in range(N):
        initial_population.append(binary_encode(random.uniform(a, b), a, b))
    return initial_population


def main():
    initial_population = select_initial_population(
        INTERVAL["LEFT_MARGIN"], INTERVAL["RIGHT_MARGIN"], INITIAL_POPULATION_SIZE
    )
    print(initial_population)
    decoded_values = []
    for i in range(INITIAL_POPULATION_SIZE):
        decoded_values.append(
            binary_decode(
                initial_population[i], INTERVAL["LEFT_MARGIN"], INTERVAL["RIGHT_MARGIN"]
            )
        )
    # print(decoded_values)
    fitness = compute_fitness(decoded_values)
    # print(fitness)
    probability = compute_probability_of_selection(fitness)
    print(probability)
    expected_count = compute_expected_count(fitness)
    # print(expected_count)
    actual_count = compute_actual_count(fitness, probability)
    print(actual_count)


main()
