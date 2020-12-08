from itertools import combinations
with open('Day1.txt', 'r') as fp:
    data = fp.read().splitlines()
numbers = [int(i) for i in data]


def findCombinations(lst, S, c):
    return [pair for pair in combinations(lst, c) if sum(pair) == S]


pair = findCombinations(numbers, 2020, 2)[0]
print(pair[0]*pair[1])
triplet = findCombinations(numbers, 2020, 3)[0]
print(triplet[0]*triplet[1]*triplet[2])
