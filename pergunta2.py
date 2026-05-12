def get_sequence_value(position: int) -> int:
  if not isinstance(position, int):
    raise TypeError("The position must be an integer.")

  if position < 1:
    raise ValueError("The position must be greater than or equal to 1.")

  return 11 + (position - 1) * 7


print(get_sequence_value(1))        # 11
print(get_sequence_value(2))        # 18
print(get_sequence_value(200))      # 1404
print(get_sequence_value(254))      # 1782
print(get_sequence_value(3542158))  # 24795110