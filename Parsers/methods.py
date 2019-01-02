from node import Node


def Swap(route, best, improved=True):
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


def total_length(route):
    """ calculate the total length of the route """
    road_length = 0
    for i in range(len(route)):
        if i < len(route) - 1:
            road_length += Node.distance(route[i], route[i+1])
    return road_length
