text = "  Hello World  "
print("Raw text:", text)

print("Length:", len(text)) # print text's amount of letters including spaces

print(text.lower()) # makes everthing lowercase
print(text.upper()) # make everthing uppercase
print(text.title()) # make starting letter of every word uppercase

print(text.strip()) # removes all spaces
print(text.rstrip()) # removes spaces from right
print(text.lstrip())# removes spaces from left


# you can combine multiple string functions at once:
print(text.strip().lower())

message = "banana bread"
print(message.count("na"))
print(message.find("bread")) # index of first match (or -1)

print(message.replace("banana", "pumpkin")) # .replace(a, b) replaces all a in text with b

print(message.startswith("ba"))
if message.endswith("bread"):
    print("Message is a bread.")