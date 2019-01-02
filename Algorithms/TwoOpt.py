from Parsers import total_length
from time import time
from graph import Graph


class Two_opt(Graph):
    """ Base on the path given by the nearest neighbor algorithm,
    this algorithm swap the path until there is no better route found """

    def two_opt(self, route):
        """ the main two opt blueprint """
        start_time = time()
        best = route
        # swap the original route until there is no better route found
        best, road_length = Two_opt.Swap(route, best)
        end_time = time()
        return [city for city in best], len(best), road_length, end_time-start_time

    @staticmethod
    def Swap(route, best, improved=True):
        """ The most important part of the two opt algorithm:
            swap a part of the route in reversed order then
            compare with the previous path """
        # loop until no better route is found
        while improved:
            improved = False
            for i in range(1, len(route)):
                for j in range(i+1, len(route)):
                    # changes nothing, skip then
                    if j-i == 1:
                        continue
                    new_route = route[:]
                    # this is the 2woptSwap
                    new_route[i:j] = route[j-1:i-1:-1]
                    if total_length(new_route) < total_length(best):
                        best = new_route
                        # better route is found
                        improved = True
            route = best
        return best, total_length(best)