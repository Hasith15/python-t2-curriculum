# a tuple is like a list, but it cannot be changed after being created (immutable)
point = (3, 5) # this is a tuple
print(point) 

print("x:", point[0])
print("y:", point[1])

red = (255, 0, 0)
print(red)
print("Length:", len(red))

# tuples can hold mixed types too
info= ("Max", 16, "Redmond")
print(info)

# you can loop through tuples too
for item in info:
    print(item)

for i in range(len(info)):
    print(info[i])