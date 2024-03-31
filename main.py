import random
from constants import *
from statistics import mean
from manim_utils import *


def do_mutation(descendants, number_of_bits, mutation_rate):
    mutated_descendants = []

    for i in range(len(descendants)):
        if random.random() < mutation_rate:
            mutation_index = random.randint(0, number_of_bits - 1)
            encoded_value = descendants[i]
            mutated_value = (
                encoded_value[:mutation_index]
                + ("1" if encoded_value[mutation_index] == "0" else "0")
                + encoded_value[mutation_index + 1 :]
            )
            mutated_descendants.append(mutated_value)
        else:
            mutated_descendants.append(descendants[i])
    return mutated_descendants


def create_offspring(
    population,
    first_parent_index,
    second_parent_index,
    number_of_bits,
):
    crossover_point = random.randint(1, number_of_bits - 1)
    first_offspring = (
        population[first_parent_index][0][:crossover_point]
        + population[second_parent_index][0][crossover_point:]
    )

    second_offspring = (
        population[second_parent_index][0][:crossover_point]
        + population[first_parent_index][0][crossover_point:]
    )

    return first_offspring, second_offspring


def do_crossover(
    sorted_population,
    crossover_rate,
    number_of_bits,
):
    population_copy = sorted_population
    descendants = []

    i = 0
    j = 1

    while j < len(sorted_population):
        first_parent = list(population_copy[i])
        second_parent = list(population_copy[j])

        first_parent[4] = first_parent[4] - 1
        second_parent[4] = second_parent[4] - 1

        population_copy[i] = tuple(first_parent)
        population_copy[j] = tuple(second_parent)

        if random.random() < crossover_rate:
            first_descendant, second_descendant = create_offspring(
                population_copy,
                i,
                j,
                number_of_bits,
            )
            descendants.append(first_descendant)
            descendants.append(second_descendant)
        else:
            descendants.append(population_copy[i][0])
            descendants.append(population_copy[j][0])

        if population_copy[i][4] == 0:
            if population_copy[j][4] == 0:
                i = i + 2
                j = j + 2
            else:
                i = i + 1
                j = j + 1
        else:
            if population_copy[j][4] == 0:
                j = j + 1

    return descendants


def sort_population(encoded_values, decoded_values, fitness, probability, actual_count):
    pairs = list(
        zip(encoded_values, decoded_values, fitness, probability, actual_count)
    )
    sorted_population = sorted(pairs, key=lambda pair: pair[2], reverse=True)
    return sorted_population


def filter_based_on_actual_count(
    encoded_values, decoded_values, fitness, probability, actual_count
):
    i = 0
    while i != len(actual_count):
        if not actual_count[i]:
            actual_count.pop(i)
            encoded_values.pop(i)
            decoded_values.pop(i)
            fitness.pop(i)
            probability.pop(i)
        else:
            i = i + 1


def compute_actual_count(probability, population_size):
    actual_count = [0] * len(probability)
    number_of_spins = population_size * 2

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


def compute_fitness(x):
    return 4 * x**4 + 3 * x**3 + 2 * x**2 + x + 1


def compute_fitness_for_population(arguments):
    fitness = []
    for i in range(len(arguments)):
        fitness.append(compute_fitness(arguments[i]))
    return fitness


def binary_decode(encoded_string, a, b, number_of_bits):
    decoded_number = int(encoded_string, 2)
    decoded_number = decoded_number / (2**number_of_bits - 1) * (b - a) + a
    return decoded_number


def binary_encode(number, a, b, number_of_bits):
    corresponding_integer = int((number - a) / (b - a) * (2**number_of_bits - 1))
    return bin(corresponding_integer)[2:].zfill(number_of_bits)


def select_initial_population(size, a, b, number_of_bits):
    population = []
    for i in range(size):
        population.append(binary_encode(random.uniform(a, b), a, b, number_of_bits))
    return population


def run_genetic_algorithm(
    initial_population_size,
    generations,
    domain_min,
    domain_max,
    number_of_bits,
    crossover_rate,
    mutation_rate,
    value_threshold,
):
    encoded_population = select_initial_population(
        initial_population_size,
        domain_min,
        domain_max,
        number_of_bits,
    )

    for generation in range(generations):
        if len(encoded_population) > 1:
            decoded_population = []
            for i in range(len(encoded_population)):
                decoded_population.append(
                    binary_decode(
                        encoded_population[i], domain_min, domain_max, number_of_bits
                    )
                )

            fitness = compute_fitness_for_population(decoded_population)

            probability = compute_probability_of_selection(fitness)

            expected_count = compute_expected_count(fitness)

            actual_count = compute_actual_count(probability, len(encoded_population))

            filter_based_on_actual_count(
                encoded_population,
                decoded_population,
                fitness,
                probability,
                actual_count,
            )

            sorted_population_based_on_fitness = sort_population(
                encoded_population,
                decoded_population,
                fitness,
                probability,
                actual_count,
            )

            decoded_values_for_animation = []
            fitness_values_for_animation = []

            for i in range(len(sorted_population_based_on_fitness)):
                decoded_values_for_animation.append(
                    sorted_population_based_on_fitness[i][1]
                )
                fitness_values_for_animation.append(
                    sorted_population_based_on_fitness[i][2]
                )

            add_generation_data(
                decoded_values_for_animation,
                fitness_values_for_animation,
                generation + 1,
            )

            best_solution = sorted_population_based_on_fitness[0]

            if best_solution[2] >= value_threshold:
                # generate_animation()
                print("A value above the threshold was found!")
                return best_solution

            descendants = do_crossover(
                sorted_population_based_on_fitness,
                crossover_rate,
                number_of_bits,
            )

            next_population = do_mutation(descendants, number_of_bits, mutation_rate)

            encoded_population = next_population

    final_decoded_population = []
    for i in range(len(encoded_population)):
        final_decoded_population.append(
            binary_decode(encoded_population[i], domain_min, domain_max, number_of_bits)
        )
    final_fitness = compute_fitness_for_population(decoded_population)
    return sorted(final_fitness, reverse=True)


def main():
    result = run_genetic_algorithm(
        INITIAL_POPULATION_SIZE,
        NUMBER_OF_GENERATIONS,
        FUNCTION_DOMAIN["MIN"],
        FUNCTION_DOMAIN["MAX"],
        NUMBER_OF_BITS,
        CROSSOVER_RATE,
        MUTATION_RATE,
        VALUE_THRESHOLD,
    )
    print(result)


main()
