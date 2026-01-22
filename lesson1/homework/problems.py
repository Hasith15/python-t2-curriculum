# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
word = input("GIVE ME A WORD:")
drow = word[::-1]
print(drow)

# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
word = input("GIVE ME A WORD:")
letter = input("GIVE ME A LETTER:")
letterinword = word.count(letter)
print("The letter appears", letterinword, "time(s) in the word.")

# Problem 3
# Ask the user for an email address like "name@example.com".
# Print only the part after the @ (example: "example.com").
email_address = input("Please enter an email address: ")
    
parts = email_address.split('@')
    
if len(parts) == 2:
    domain_name = parts[1]
    print("The domain part is:", domain_name)
else:
        print("Invalid email format entered. Please include one '@' symbol.")


# Problem 4
# Ask the user for a word.
# Print the word without the first and last character.
word = input("GIVE ME A WORD:")
word_is_now_or = word[1:-1]
print(word_is_now_or)
# Problem 5
# Ask the user for a sentence.
# Print "Long" if the sentence has more than 20 characters (including spaces),
# otherwise print "Short".
sentence = input("GIMME A SENTENCE")
if len(sentence) > 20:
      print("Long")
else:
      print("Short")