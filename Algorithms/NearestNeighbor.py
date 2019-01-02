from graph import Graph
from Parsers import total_length
from node import Node
from time import time


class Nearest_neighbor(Graph):
    """ This class inherits from the Graph class """

    def nearest_neighbor(self):
        # for calculating the run-time of the algorithm
        start_time = time()
        city_info = self.get_all_nodes()
        # the start point is the first city in the list of Nodes city_info
        start = city_info[0]
        path = [start]
        city_info.remove(start)
        # loop until the city_info list is empty
        while city_info:
            """ find the closest city by calculating the distances between the start Node
                and each city in the list then get the shortest distance"""
            closest_city = min(city_info, key=lambda city: Node.distance(city, start))
            # add the closest city to the path
            path.append(closest_city)
            # then continue the loop with the start point as the last city
            start = closest_city
            city_info.remove(start)
        end_time = time()
        return path, [city for city in path], len(path), total_length(path), end_time-start_time
