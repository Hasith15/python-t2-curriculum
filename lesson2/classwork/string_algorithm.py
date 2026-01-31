# counting vowels in a word
word = "mississipi"
vowels = "aeiou"
counter = 0
for character in word:
    if character in vowels:
        counter = counter + 1
print("Vowel count:", counter)

# A palindrone is a word that is the same forwards and backwards
test = "racecar"
backwards = test[::1]
if test == backwards:
    print("Word is a palindrone")
else:
    print("Word is NOT a palindrone")

# Counting digits inside a word
word2 = "15pineapple343"
digits = "1234567890"
counter2 = 0
for character in digits:
    if character in digits:
        counter2 = counter2 + 1
print(counter2)

#counting occurences of a letter in a word
word3 = "Orange"
counter3 = 0
for character in word3:
    if character in word3:
        counter3 = counter3 + 1
print(counter3)