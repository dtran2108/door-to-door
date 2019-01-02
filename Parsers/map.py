from sys import stderr, exit


def print_error():
  """ print the Invalid file error """
  print('Invalid file', file=stderr)
  exit()


def check_file_format(lst):
  """ check if the file is probably formated """
  for check in lst:
    if len(check) < 3 or len(check) > 3:
      print_error()
    try:
      float(check[1])
      float(check[2])
    except Exception:
      print_error()


def check_file(file_name):
  """ check for File Existence and 
      File Permission """
  try:
    f = open(file_name, 'r')
  except Exception:
    print_error()
  return f


def get_map(file_name):
  """ return a list contains the lists in which 
      each of them has three elements: city name,
      latitude, longtitude """
  f = check_file(file_name)
  content = f.read().splitlines()
  city_map = [line.split(', ') for line in content]
  # check if the file is properly formatted
  check_file_format(city_map)
  return city_map
