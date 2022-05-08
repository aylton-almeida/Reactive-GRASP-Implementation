import time
from typing import Callable


class BaseAlgorithm:
    """Class representing a base algorithm implementation"""

    restriction_size: int
    population_size: int

    population: list[int]
    calc_fitness: Callable[[list[int]], int]

    solution: list[int]
    duration: int

    def __init__(
        self,
        population: list[int],
        calc_fitness: Callable[[list[int]], int],
        population_size: int = 100,
        restriction_size: int = 10
    ) -> None:
        self.population = population
        self.calc_fitness = calc_fitness
        self.population_size = population_size
        self.restriction_size = restriction_size

    def init_timer(self):
        """Initializes the timer"""

        self.duration = time.time()

    def stop_timer(self):
        """Finishes the timer"""

        self.duration = round(time.time() - self.duration, 2)

    def run(self):
        """Runs this for the given population and result size"""

        raise NotImplementedError()

    def __repr__(self) -> str:
        return f'{self.solution} -> {self.calc_fitness(self.solution)}' + \
            f'\nDuration: {self.duration} seconds'
