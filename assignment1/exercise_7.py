# Exercise 7: Extract Length of Each Word in Sentences

sentences = [
    "Python is awesome",
    "Lambda functions are powerful",
    "Map applies transformations"
]

# extract the length of each word in every sentence using nested map()
word_lengths = list(map(
    lambda sentence: list(map(lambda word: len(word), sentence.split())),
    sentences
))

print("Sentences and their word lengths:\n")
for i in range(len(sentences)):
    print(f"Sentence {i+1}: '{sentences[i]}'")
    print(f"Word lengths: {word_lengths[i]}\n")