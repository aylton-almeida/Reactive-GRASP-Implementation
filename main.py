"""This algorithm will generate a list of random numbers
    and run it through some algorithms to
    will find the best solution for the given equation
    ∑(n^2 / n - 1)
"""

import random

from algorithms.BaseAlgorithm import BaseAlgorithm
from algorithms.Greedy import Greedy
from algorithms.Random import Random
from algorithms.ReactiveGrasp import ReactiveGRASP
from algorithms.Sorting import Sorting

POPULATION_SIZE = 100
RESTRICTION_SIZE = 10


def generate_population():
    """Generate a list of n random numbers, they we'll be our population"""

    return [
        random.randint(0, 100)
        for _ in range(POPULATION_SIZE)
    ]


def calc_fitness(current_solution: list[int]):
    """Fitness functions that calculate the problem equation
        (∑(n^2 / n - 1)) for the given solution
    """

    return sum([
        value ** 2 /
        1 if index == 0 else current_solution[index - 1]
        for index, value in enumerate(current_solution)
    ])


def run_algorithm(algorithm: BaseAlgorithm, population: list[int]):
    """Run the given algorithm and prints result"""

    instance: BaseAlgorithm = algorithm(
        population.copy(),
        calc_fitness,
        POPULATION_SIZE,
        RESTRICTION_SIZE
    )
    instance.run()
    print(f'{algorithm.__name__}: {instance}\n')


def main():
    """Main function"""

    population = generate_population()

    for algorithm in [ReactiveGRASP, Sorting, Greedy, Random]:
        run_algorithm(algorithm, population)


if __name__ == '__main__':
    main()
