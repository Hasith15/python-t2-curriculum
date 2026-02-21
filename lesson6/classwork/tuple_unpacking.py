point = (8, 2)
x, y = point
print("x is", x)
print("y is", y)

# Swapping values with tuples
a = 5
b = 9
a, b = b, a
print(a, b)

# Returning multiple values from a function (as a tuple):
def min_and_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    return smallest, largest

nums = [1, 2, 3, 4, 5]
mn, mx = min_and_max(nums)
print("Min:", mn)
print("Max:", mx)