# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
n = int(input("Give me a number:"))
print("All numbers divisible to the number are the following:")
for i in range(0, n):
    if i % 3 == 0:
        print(i)
if n % 3 == 0:
    print(n)

# Problem 2
# Ask the user for a number n.
# Print the square of every number from 1 to n (1*1, 2*2, ...).
n = int(input("Give me a number: "))

for i in range(1, n + 1):
    print(i * i)

# Problem 3
# Ask the user for a number n.
# Print the numbers from n down to 0 (counting down).
n = int(input("Give me a number"))

while n >= 0:
    print(n)
    n = n - 1

# Problem 4
# Ask the user for a word.
# Build a new string that repeats the word 5 times with spaces in between.
# Example: "hi hi hi hi hi"
for_a_word = input("Give me a word")
word = for_a_word + " "
print(word * 5)

# Problem 5
# Ask the user for a number n.
# Print how many numbers from 1 to n are even.
n = int(input("Give me a number"))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)