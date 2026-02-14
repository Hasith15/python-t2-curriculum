scores = {
    "Ava": 95,
    "Ben": 88,
    "Kai": 73
}

# loop through keys
for name in scores:
    print(name, "scored", scores[name])

# get a list of the keys
print(list(scores.keys()))

# get a list of the values
print(list(scores.values()))

# get a list of both keys and values
print(list(scores.items()))

# looping through keys & values
for name, score in scores.items():
    if score >= 90:
        print(name, "got an A")

# loop throungh only values
for value in scores.values():
    print(value)

# loop throungh only keys
for key in scores.values():
    print(key)