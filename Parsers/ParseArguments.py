from argparse import ArgumentParser
from Algorithms import Two_opt, Nearest_neighbor


def parse_argument():
  parser = ArgumentParser(description='Traveling Salesman Problem')
  parser.add_argument('FILENAME', help='the file contains a list of city\
                      you want to travel', type=str)
  parser.add_argument('--algo', help='specify which algorithm to use for\
                      finding the path among [nearest_neighbor|two_opt],\
                      default: all',
                      type=str, dest='ALGO', default='all')
  args = parser.parse_args()
  filename = args.FILENAME
  algo = args.ALGO
  return algo, filename


def implement_nneighbor(city_map):
  print('NEAREST NEIGHBOR:')
  _, path, number_of_city, len_road, run_time = Nearest_neighbor.nearest_neighbor(city_map)
  city_map.display_graph(path, number_of_city, len_road, run_time)


def implement_2opt(city_map):
  print('TWO OPT:')
  route, _, _, _, _ = Nearest_neighbor.nearest_neighbor(city_map)
  path, number_of_city, len_road, run_time = Two_opt.two_opt(city_map, route)
  city_map.display_graph(path, number_of_city, len_road, run_time)


def implement_algorithm(algorithm, city_map):
  if algorithm == 'nearest_neighbor':
    implement_nneighbor(city_map)

  elif algorithm == 'two_opt':
    implement_2opt(city_map)

  elif algorithm == 'all':
    implement_nneighbor(city_map)
    print('='*80)
    implement_2opt(city_map)
