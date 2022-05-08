from random import choice

from algorithms.BaseAlgorithm import BaseAlgorithm


class Random(BaseAlgorithm):
    """Class representing a random algorithm implementation"""

    def run(self):

        self.init_timer()

        self.solution = []

        for _ in range(self.restriction_size):
            element = choice(self.population)

            self.population.pop(self.population.index(element))

            self.solution.append(element)

        self.stop_timer()
