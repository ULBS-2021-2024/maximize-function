# Genetic Algorithm Optimization

## Introduction

This project implements a genetic algorithm optimization technique in Python that maximizes the function $4 \cdot x^4 + 3 \cdot x^3 + 2 \cdot x^2 + x^1 + 1$. 

## Technical


A genetic algorithm is a powerful optimization technique inspired by the process of natural selection and genetics. It's designed to find solutions to optimization and search problems by mimicking the principles of biological evolution. At its core, a genetic algorithm operates on a population of candidate solutions, represented as individuals or chromosomes, which undergo a process of evolution over generations to improve their fitness.

In the context of maximizing functions, a genetic algorithm aims to find the input parameters or configurations that produce the maximum output value of a given function, often referred to as the objective function or fitness function. Each individual in the population represents a potential solution to the optimization problem, and its fitness is evaluated based on how well it performs according to the objective function. The genetic algorithm then iteratively explores the search space, selecting individuals with higher fitness to serve as parents for producing offspring through genetic operations such as crossover and mutation.

Through these genetic operations, the algorithm introduces variations and explores new regions of the search space, gradually improving the population's overall fitness over generations. As the algorithm progresses, individuals with higher fitness become more prevalent in the population, leading to the convergence towards the optimal solution.

## Technologies used

* Python: Python was chosen as the primary programming language for this project due to its ease of use, extensive libraries, and fast development workflow. Python's simplicity and readability make it an ideal choice for implementing complex algorithms like genetic algorithms. Additionally, the vast ecosystem of libraries in Python provides powerful tools for numerical computation, data visualization, and algorithmic optimization, facilitating efficient implementation and experimentation.

* Manim: Manim (Mathematical Animation Engine) is a powerful Python library for creating animations, particularly suited for mathematical and scientific visualization. The decision to incorporate Manim into the project was driven by the desire to visualize the genetic algorithm's operations and results in a clear and engaging manner. By leveraging Manim's capabilities, the project aims to provide visual insights into how the genetic algorithm progresses through generations, how candidate solutions evolve, and how the fitness landscape changes over time.

	Here you can see the graph of the function animated using manim:

	<details>
	<summary>Function Graph</summary>
		<video controls src="out/FunctionAnimation.mp4" title="Title"></video>
	</details>

## Algorithm

The algorithm is implemented in 10 steps:

1. Select a random initial population from the function chosen domain, encoded in binary, into a finite length string
2. Obtain the decoded x values for the initial population generated. 
3. Calculate the fitness or objective function.
4. Compute the probability of selection,
5. The next step is to calculate the expected count, which is calculated as,
6. Now the actual count is to be obtained to select the individuals, which would
participate in the crossover cycle using Roulette wheel selection. The Roulette wheel is formed as shown in Fig. 3.24.
7. Now, writing the mating pool based upon the actual count as shown in
8. Crossover operation is performed to produce new offspring (children).
9. After crossover operations, new off springs are produced and ‘x’ values are
decodes and fitness is calculated.
10. In this step, mutation operation is performed to produce new off springs
after crossover operation. As discussed in Sect. 3.10.3.1 mutation-flipping operation is performed and new off springs are produced. Table 3.3 shows the new offspring after mutation.

## Tests

1. 

```python
INITIAL_POPULATION_SIZE = 8
NUMBER_OF_GENERATIONS = 50
FUNCTION_DOMAIN = {"MIN": -198, "MAX": 201}
NUMBER_OF_BITS = 5
MUTATION_RATE = 0.01
VALUE_THRESHOLD = 6424080201
```

<details>
 <summary>Result</summary>
	<video controls src="tests/Test1.mp4" title="Title"></video>
</details>


# Bibliography

[Introduction to Genetic Algorithms by S.N. Sivanandam, S.N. Deepa](<doc/Introduction to Genetic Algorithms, Springer.pdf>)