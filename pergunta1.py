def starts_with_b_and_ends_with_a(text: str) -> bool:
  if not isinstance(text, str):
    raise TypeError("The input must be a string.")

  return text.startswith("B") and text.endswith("A")


print(starts_with_b_and_ends_with_a("BOLA"))    # True
print(starts_with_b_and_ends_with_a("BANANA"))  # True
print(starts_with_b_and_ends_with_a("banana"))  # False