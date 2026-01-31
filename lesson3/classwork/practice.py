# Problem 1
# Use a for loop with range to print every number from 5 to 12 (including 12).
for i in range(5, 13):
    print(i)


# Problem 2
# Use range with step to print all even numbers from 0 to 20 (including 20).
print("________________________________________________________________________________________________________________________________________")
for i in range(0, 21, 2):
    print(i)

# Problem 3
# Ask the user for a number n.
# Print the sum of all numbers from 1 to n (including n).
print("________________________________________________________________________________________________________________________________________")
n = input("GIMME A NUMBER")
total = 0
intn= int(n)
for i in range(1, intn + 1):
    total = i + 1
print("total:", total)
# Problem 4
# Print a countdown from 10 to 1 (10, 9, 8, ... 1).
print("________________________________________________________________________________________________________________________________________")
for i in range(10, 0, -1):
    print(i)

# Problem 5
# Ask the user for a word.
# Print each character with its index on a new line.
# Example: 0 h, 1 e, 2 l, ...
print("________________________________________________________________________________________________________________________________________")
a_word = input("GIVE ME A WORD")
for i in range(len(a_word)):
    print(" ")