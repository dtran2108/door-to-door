from node import Node


def total_length(route):
    """ calculate the total length of the route """
    road_length = 0
    for i in range(len(route)):
        if i < len(route) - 1:
            road_length += Node.distance(route[i], route[i+1])
    return road_length
