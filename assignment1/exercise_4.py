# Exercise 4: Extract First and Last Characters

words = ["python", "lambda", "programming", "map", "function"]

# Create tuples of (first_char, last_char) for each word
char_tuples = list(map(lambda c: (c[0], c[-1]), words))

print("Words:")
print(words)
print("\n(First, Last) character tuples:")
print(char_tuples)
print("\nExpected Output: [('p', 'n'), ('l', 'a'), ('p', 'g'), ('m', 'p'), ('f', 'n')]")