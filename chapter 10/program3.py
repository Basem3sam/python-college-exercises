def filter_positive():
  while True:
    num = yield
    if num > 0:
      print(f"Positive number: {num}")

# Test
co = filter_positive()
next(co)  # Prime the coroutine
co.send(-3)
co.send(5)
co.send(0)