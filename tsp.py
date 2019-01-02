#!/usr/bin/env python3
from Parsers import get_map, parse_argument, implement_algorithm
from graph import Graph


def main():
  algo, filename = parse_argument()
  city_map = Graph(get_map(filename))
  implement_algorithm(algo, city_map)
    
  
if __name__ == '__main__':
    main()