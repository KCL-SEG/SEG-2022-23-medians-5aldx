"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numbers.sort()

x = len(numbers)
if x%2 == 0:
    y = numbers[x//2]+ numbers[(x//2)-1]
    print(y/2)
else:
    print(numbers[x//2])
