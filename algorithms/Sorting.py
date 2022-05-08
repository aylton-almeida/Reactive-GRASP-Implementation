from algorithms.BaseAlgorithm import BaseAlgorithm


class Sorting(BaseAlgorithm):
    """Class representing a Sorting algorithm implementation"""

    def run(self):

        self.init_timer()

        self.population.sort(reverse=True)
        self.solution = self.population[:self.restriction_size]

        self.stop_timer()
