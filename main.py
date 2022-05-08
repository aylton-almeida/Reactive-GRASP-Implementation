"""This algorithm will generate a list of random numbers
    and run it through a Reactive GRASP algorithm that
    will find the best solution for the given equation
    ∑(n^2 / n - 1)
"""

import random
from statistics import mean


def calc_fitness(current_solution: list[int]):
    """Fitness functions that calculate the problem equation
        (∑(n^2 / n - 1)) for the given solution
    """

    return sum([
        value ** 2 /
        1 if index == 0 else current_solution[index - 1]
        for index, value in enumerate(current_solution)
    ])


def calc_alpha(current_population: list[int], solution: list[int]):
    """Calculates alpha probability for given population"""

    return calc_fitness(solution) / mean([calc_fitness(current_population[:index + 1]) for index, _ in enumerate(current_population)])


class ReactiveGRASP:
    """Class representing a Reactive GRASP algorithm implementation"""

    restriction: int
    population_size: int

    initial_population: list[int]
    population: list[int]
    alpha: list[int]

    solution: list[int]

    def __init__(self, population_size: int = 100, restriction: int = 10) -> None:
        self.population_size = population_size
        self.restriction = restriction

        self.generate_population()

    def generate_population(self):
        """Generate a list of n random numbers, they we'll be our population"""

        self.population = [
            random.randint(0, 100)
            for _ in range(self.population_size)
        ]

        self.initial_population = self.population.copy()

    def update_alpha_probabilities(self):
        """Updates the alpha probabilities for the next iteration"""

        # ! Really don't think this is fully correct

        # If it's the first iteration, set all probabilities as the same
        # else, calculate the new probabilities for each item in the population
        if not self.alpha:
            self.alpha = [
                1 / self.population_size
                for _ in range(self.population_size)
            ]

        else:
            qi = calc_alpha(self.initial_population, self.solution)

            self.alpha = [
                qi / calc_alpha(self.population, self.population[:index + 1])
                for index, _ in enumerate(self.population)
            ]

    def construction_phase(self) -> list[int]:
        """Runs the construction phase of the GRASP algorithm"""

        previous_solution_fitness = calc_fitness(self.solution)

        new_element: int = None

        while new_element is None:
            # fetch element at random from the population based on alpha probabilities
            new_element = random.choices(self.population, self.alpha)[0]

            # if it's better than the current solution, add it to the solution
            if calc_fitness(self.solution + [new_element]) > previous_solution_fitness:
                self.population.pop(self.population.index(new_element))
                self.solution.append(new_element)

            else:
                new_element = None

        self.update_alpha_probabilities()

    def local_search(self) -> list[int]:

        return []

    def run(self):
        """Runs the GRASP algorithm for the given population and result size"""

        self.solution = []
        self.alpha = []

        self.update_alpha_probabilities()

        for _ in range(self.restriction):
            self.construction_phase()
            new_solution = self.local_search()
            if calc_fitness(new_solution) > calc_fitness(self.solution):
                self.solution = new_solution

    def __repr__(self) -> str:
        return f'{self.solution} -> {calc_fitness(self.solution)}'


def main():
    """Main function"""

    grasp = ReactiveGRASP()

    grasp.run()

    print(grasp)

    # population = generate_population(100)

    # solution = grasp(population, 10)

    # print(f'{solution} -> {fitness(solution)}')

    # for _ in range(10):
    #     population = generate_random_numbers(100)

    #     print(f'{population[:10]} -> {fitness(population[:10])}')
    #     population.sort(reverse=True)
    #     print(f'{population[:10]} -> {fitness(population[:10])}')
    #     print()


if __name__ == '__main__':
    main()
