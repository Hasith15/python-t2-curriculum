# building a string with a loop (string concattenation)
name = "Max"
result = ""
for character in name: # For each loop: iterates over every element
    result = result + character + "-"
print(result)

# build string by collecting pieces in a list, then joining
letters = ["a", "p", "p", "l", "e"]
built = "".join(letters) # .join(): building string from list, uses seperator whick function is called on
print(built)

# make a new string with only the even index characters
word = "dogs"
new_word = ""
for i in range(len(word)): # 0, 1, 2, 3
    if i % 2 == 0:
        new_word = new_word + word[i]
print(new_word)