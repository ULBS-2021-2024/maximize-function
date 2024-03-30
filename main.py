import random
from constants import *
from statistics import mean


def do_mutation(descendants):
    mutation_rate = 0.01
    mutated_descendants = []
    for i in range(len(descendants)):
        descendant = list(descendants[i])
        if random.random() < mutation_rate:
            mutation_index = random.randint(0, NUMBER_OF_BITS)
            encoded_value = descendant[0]
            encoded_value = (
                encoded_value[:mutation_index]
                + ("1" if encoded_value[mutation_index] == "0" else "0")
                + encoded_value[mutation_index + 1 :]
            )
            decoded = binary_decode(
                encoded_value, INTERVAL["LEFT_MARGIN"], INTERVAL["RIGHT_MARGIN"]
            )
            fitness = evaluate_function(decoded)
            mutated_descendants.append(tuple((encoded_value, decoded, fitness)))
        else:
            mutated_descendants.append(descendant[i])
    return mutated_descendants


def create_offspring(copy, i, j):
    crossover_point = random.randint(1, NUMBER_OF_BITS)
    offspring1 = copy[i][0][:crossover_point] + copy[j][0][crossover_point:]
    offspring2 = copy[j][0][:crossover_point] + copy[i][0][crossover_point:]
    dv1 = binary_decode(offspring1, INTERVAL["LEFT_MARGIN"], INTERVAL["RIGHT_MARGIN"])
    dv2 = binary_decode(offspring2, INTERVAL["LEFT_MARGIN"], INTERVAL["RIGHT_MARGIN"])
    fitness1 = evaluate_function(dv1)
    fitness2 = evaluate_function(dv2)
    child1 = tuple((offspring1, dv1, fitness1))
    child2 = tuple((offspring2, dv2, fitness2))
    return child1, child2


def do_crossover(sorted_fitness):
    copy = sorted_fitness
    descendants = []
    i = 0
    j = 1
    while j != len(sorted_fitness):
        d1, d2 = create_offspring(copy, i, j)
        descendants.append(d1)
        descendants.append(d2)

        copied_pair_list_1 = list(copy[i])  # Convert the pair to a list to modify it
        copied_pair_list_2 = list(copy[j])
        copied_pair_list_1[4] = copied_pair_list_1[4] - 1  # decrease actual count
        copied_pair_list_2[4] = copied_pair_list_2[4] - 1  # decrease actual count
        copy[i] = tuple(copied_pair_list_1)
        copy[j] = tuple(copied_pair_list_2)
        if copy[i][4] == 0:
            if copy[j][4] == 0:
                i = i + 2
                j = j + 2
            else:
                i = i + 1
                j = j + 1
        else:
            if copy[j][4] == 0:
                j = j + 1
    return descendants


def sort_fitness(encoded_values, decoded_values, fitness, probability, actual_count):
    pairs = list(
        zip(encoded_values, decoded_values, fitness, probability, actual_count)
    )
    sorted_fitness = sorted(pairs, key=lambda pair: pair[2], reverse=True)
    return sorted_fitness


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


def compute_actual_count(fitness, probability):
    actual_count = [0] * len(probability)
    number_of_spins = INITIAL_POPULATION_SIZE * 2

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
    decoded_number = int(binary_string, 2)
    decoded_number = decoded_number / (2**NUMBER_OF_BITS - 1) * (b - a) + a
    return decoded_number


def binary_encode(x, a, b):
    corresponding_integer = int((x - a) / (b - a) * (2**NUMBER_OF_BITS - 1))
    return bin(corresponding_integer)[2:].zfill(NUMBER_OF_BITS)


def select_initial_population(a, b, N):
    initial_population = []
    for i in range(N):
        initial_population.append(binary_encode(random.uniform(a, b), a, b))
    return initial_population


def main():
    initial_population = select_initial_population(
        INTERVAL["LEFT_MARGIN"], INTERVAL["RIGHT_MARGIN"], INITIAL_POPULATION_SIZE
    )
    # print(initial_population)
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
    # print(probability)
    expected_count = compute_expected_count(fitness)
    # print(expected_count)
    actual_count = compute_actual_count(fitness, probability)
    # print(actual_count)
    filter_based_on_actual_count(
        initial_population, decoded_values, fitness, probability, actual_count
    )

    sorted_fitness = sort_fitness(
        initial_population, decoded_values, fitness, probability, actual_count
    )

    # crossover
    descendants = do_crossover(sorted_fitness)
    # print(descendants)
    next_population = do_mutation(descendants)
    print(next_population)


main()
