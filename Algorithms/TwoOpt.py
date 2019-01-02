from Parsers import Swap
from time import time
from graph import Graph


class Two_opt(Graph):
    """ This class inherits from the Graph class """

    def two_opt(self, route):
        # for calculating the run-time of this algorithm
        start_time = time()
        best = route
        # swap the original route until there is no better route found
        best, road_length = Swap(route, best)
        end_time = time()
        return [city for city in best], len(best), road_length, end_time-start_time
