from node import Node


class Graph:
    def __init__(self, city_map):
        self.city_map = city_map

    def get_all_nodes(self):
        """ turn all the elements of the list city_map into Node objects """
        return [Node(x) for x in self.city_map]

    def display_graph(self, path, number_of_city, len_road, run_time):
        """ display the graph for easier look """
        for i, city in enumerate(path):
            if i == len(path) - 1:
                print(city, end='\n\n')
            else:
                print(city, end=' - ')
        print('length of the road: {}'.format(len_road))
        print('number of cities visited: {}'.format(number_of_city))
        print('run-time: {}s'.format(run_time))
