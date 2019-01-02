from sys import stderr, exit


def check_file_format(lst):
  for check in lst:
    if len(check) < 3 or len(check) > 3:
      print('Invalid file', file=stderr)
      exit(0)


def check_file(file_name):
  """ check for File Existence and 
      File Permission """
  try:
    f = open(file_name, 'r')
  except Exception:
    print('Invalid file', file=stderr)
    exit(0)
  return f


def get_map(file_name):
  f = check_file(file_name)
  content = f.read().splitlines()
  city_map = [line.split(', ') for line in content]
  # check if the file is properly formatted
  check_file_format(city_map)
  return city_map
