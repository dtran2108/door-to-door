class Node:
  def __init__(self, city_info):
    self.city_name = city_info[0]
    self.city_pos = (float(city_info[1]), float(city_info[2]))

  def __repr__(self):
    """ return the city name for ambigous city calling """
    return self.city_name

  def get_position(self):
    """ return the latitude and longtitude 
        of the city """
    return self.city_pos

  @staticmethod
  def distance(city1, city2):
    """ return the Eucilean distance between city1 and city2 """
    city1_coordinate = city1.get_position()
    city2_coordinate = city2.get_position()
    return ((city1_coordinate[0] - city2_coordinate[0])**2 + 
            (city1_coordinate[1] - city2_coordinate[1])**2)**0.5
