import math

def polysum(n, s):
  """
  A regular polygon has n number of sides. Each side has length s.
  The area of a regular polygon is: (0.25 * n * s ** 2) / tan(π / n).
  The perimeter of a polygon is: length of the boundary of the polygon.
  This function is for calculating the polysum of a regular polygon.
  """
  # get area
  area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
  # get perimeter
  perimeter = n * s
  # sum them up
  result = area + perimeter ** 2
  # round the sum to 4 decimals
  return round(result, 4)