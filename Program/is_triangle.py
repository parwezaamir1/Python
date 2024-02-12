def is_triangle(a, b, c):
  """
  Checks if three angles can form a triangle.

  Args:
      a: Angle in degrees (must be an integer or float).
      b: Angle in degrees (must be an integer or float).
      c: Angle in degrees (must be an integer or float).

  Returns:
      True if the angles can form a triangle, False otherwise.
  """
  return (0 < a < 180 and 0 < b < 180 and 0 < c < 180 and a + b + c == 180)

# Test the function for specific scenarios
angles_to_test = [
    (-10, 50, 130),  # Invalid angles
    (0, 90, 90),
    (200, 50, 30),
    (50, 50, 80),  # Invalid sum
    (120, 40, 30),
    (90, 45, 45),  # Valid triangles
    (60, 60, 60),
    (110, 40, 30),
    (89, 89, 2)
]

for a, b, c in angles_to_test:
  result = is_triangle(a, b, c)
  print(f"Angles: ({a}, {b}, {c}), Can form triangle?: {result}")
