# Problem 1
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).
GIVENWORD = input("GIVE A WORD TO ME")
vowels = "aeiou"
counter = 0
for character in GIVENWORD:
    if character in vowels:
            counter = counter + 1
print(counter)
# Problem 2
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".
MaybePalindrome = input("Give me a word")
emordnilaPebyaM = MaybePalindrome[::-1]
if MaybePalindrome[::-1] == emordnilaPebyaM:
      print("Palindrome")
else:
        print("Not palindrome")
# Problem 3
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).



# Problem 4
# Ask the user for two words.
# Print the two words combined with a dash in the middle. Example: "cat-dog".



# Problem 5
# Ask the user for a phrase.
# Build a new string that removes all spaces.
