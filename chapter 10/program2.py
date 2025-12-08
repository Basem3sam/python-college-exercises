def even_numbers(n):
  for i in range(2, n + 1, 2):
    yield i

# Test
for num in even_numbers(10):
  print(num)