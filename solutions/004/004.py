def solve(array_numbers):
    positive_integers = list(dict.fromkeys(
        [i for i in sorted(array_numbers) if i > 0]))

    if len(positive_integers) == 0:
        return 1
    elif len(positive_integers) == positive_integers[len(positive_integers)-1]:
        return positive_integers[len(positive_integers)-1] + 1
    else:
        for i in range(1, len(positive_integers) + 1):
            if i not in positive_integers:
                return i


assert solve([3, 4, -1, 1]) == 2
assert solve([3, 4, 4, -1, 1]) == 2
assert solve([1, 2, 0]) == 3
assert solve([1, 2, 2, 1, 0]) == 3
assert solve([1, 2, 5, 5, 6, 7]) == 3
assert solve([1]) == 2
assert solve([-1, -2]) == 1
assert solve([]) == 1
