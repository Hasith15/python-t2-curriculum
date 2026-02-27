# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.
scores = (85, 95, 13, 47)
average = sum(scores) / len(scores)
print(average)

# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
students = [("Ava", 95), ("Ben", 88), ("Kai", 73)]
top_student = max(students, key=lambda x: x[1])
print(top_student[0], "has the highest score.")

# Problem 3
# Ask the user for a sentence.
# Split it into words.
# Create a list of tuples where each tuple is (word, length_of_word).
# Print the list.
sentence = input("Please enter a sentence: ")
words = sentence.split()
word_length_list = [(word, len(word)) for word in words]
print(word_length_list)

# Problem 4
# Create a function called first_and_last(word).
# It should return a tuple containing the first and last letter of the word.
# Test it.
def first_and_last(word):
    if not word:
        return (None, None) # Handle empty strings gracefully
    return (word[0], word[-1])
word = "programming"
print("First and last of ", word, ":", first_and_last(word))

# Problem 5
# Tuples can be dictionary keys.
# Create a dictionary where the keys are points like (x, y) and the values are colors.
# Add at least 3 points and print the dictionary.
point_colors = {
    (0, 0): "Red",
    (1, 1): "Blue",
    (10, 20): "Green"
}
point_colors[(5, 5)] = "Yellow"
print(point_colors)