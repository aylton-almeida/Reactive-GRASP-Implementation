import random
from statistics import mean
from typing import Callable

from algorithms.BaseAlgorithm import BaseAlgorithm


class ReactiveGRASP(BaseAlgorithm):
    """Class representing a Reactive GRASP algorithm implementation"""

    initial_population: list[int]
    alpha: list[int]

    def __init__(
        self,
        population: list[int],
        calc_fitness: Callable[[list[int]], int],
        population_size: int = 100,
        restriction_size: int = 10
    ) -> None:
        super().__init__(population, calc_fitness, population_size, restriction_size)
        self.initial_population = population.copy()

    def calc_alpha(self, current_population: list[int], current_solution: list[int]):
        """Calculates alpha probability for given population"""

        return self.calc_fitness(current_solution) / \
            mean([
                self.calc_fitness(current_population[:index + 1])
                for index, _ in enumerate(current_population)
            ])

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
            qi = self.calc_alpha(self.initial_population, self.solution)

            self.alpha = [
                qi / self.calc_alpha(self.population,
                                     self.population[:index + 1])
                for index, _ in enumerate(self.population)
            ]

    def construction_phase(self) -> list[int]:
        """Runs the construction phase of the GRASP algorithm"""

        previous_solution_fitness = self.calc_fitness(self.solution)

        new_element: int = None

        while new_element is None:
            # create a candidate list based on the given alpha probabilities
            candidate_list = random.choices(self.population, self.alpha, k=10)

            # select the best candidate
            new_element = max(candidate_list, key=lambda element: self.calc_fitness(
                self.solution + [element]))

            # if it's better than the current solution, add it to the solution
            if self.calc_fitness(self.solution + [new_element]) > previous_solution_fitness:
                self.population.pop(self.population.index(new_element))
                self.solution.append(new_element)

            else:
                new_element = None

        self.update_alpha_probabilities()

    def local_search(self, local_solution: list[int]) -> list[int]:
        """Tries switching the first element in the list around for a better solution"""

        # Create local solution list for all possible values and solutions that can be found
        # by simply reordering the first element
        local_solutions_fitness = [
            (local_solution.copy(), self.calc_fitness(local_solution))
        ]

        first_value = local_solution.pop(0)

        for index in range(len(local_solution)):
            local_solution.insert(index, first_value)
            local_solutions_fitness.append((
                local_solution.copy(),
                self.calc_fitness(local_solution)
            ))
            local_solution.pop(index)

        return max(local_solutions_fitness, key=lambda solution: solution[1])[0]

    def run(self):

        self.init_timer()

        self.solution = []
        self.alpha = []

        self.update_alpha_probabilities()

        for _ in range(self.restriction_size):
            self.construction_phase()
            new_solution = self.local_search(self.solution.copy())
            self.solution = new_solution

        self.stop_timer()
