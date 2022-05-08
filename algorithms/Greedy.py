from algorithms.BaseAlgorithm import BaseAlgorithm


class Greedy(BaseAlgorithm):
    """Class representing a Greedy algorithm implementation"""

    def run(self):

        self.init_timer()

        self.solution = []

        for _ in range(self.restriction_size):
            best = max(self.population)

            self.population.pop(self.population.index(best))

            self.solution.append(best)

        self.stop_timer()
