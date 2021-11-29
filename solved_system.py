def is_solved(puzzle):
    i = 0
    res = 0
    while i < len(puzzle):
        # if zero auto res++
        if puzzle[i] == 0:
            res += 1
            i += 1
            continue
        # if last box break while
        i2 = i + 1
        if i2 >= len(puzzle):
            break
        # if i > i2 res++
        while i2 < len(puzzle):
            if puzzle[i] > puzzle[i2]:
                res += 1
            i2 += 1
        i += 1
    # if res % 2 == 0 => solved else unsolved
    return res % 2 == 0


print(is_solved([0, 2, 4, 1, 8, 5, 3, 6, 7]))  # unsolved
print(is_solved([5, 8, 6, 7, 0, 2, 3, 4, 1]))  # solved
print(is_solved([8, 1, 3, 4, 5, 2, 0, 7, 6]))  # solved
print(is_solved([0, 3, 8, 1, 4, 7, 6, 5, 2]))  # solved
print(is_solved([0, 8, 3, 5, 7, 1, 4, 6, 2]))  # unsolved
