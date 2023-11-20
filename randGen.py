import random

numberOfVals = 10
rangeLower = 1
rangeHigher = 100

# numberOfVals = int(input("How many random numbers? "))
# rangeLower = int(input("What's the lower range? "))
# rangeHigher = int(input("What's the higher range? "))

randomNumbers = []
for cycle in range(numberOfVals):
    randomNumbers.append(random.randrange(rangeLower, rangeHigher))
print(randomNumbers)
