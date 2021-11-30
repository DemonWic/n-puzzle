def is_solved(puzzle, size, solved):
    i = 0
    res = 0
    while i < len(puzzle):
        # if last box break while
        i2 = i + 1
        if i2 >= len(puzzle):
            break
        # if i > i2 res++
        while i2 < len(puzzle):
            n1 = puzzle[i]
            n2 = puzzle[i2]

            if solved.index(n1) > solved.index(n2):
                res += 1
                # print("res")
            i2 += 1
        i += 1
    # if res % 2 == 0 => get_solved else unsolved

    # res += get_zero_sol(puzzle, size)
    print("res: ", res)

    puzzle_zero_row = puzzle.index(0) // size
    puzzle_zero_column = puzzle.index(0) % size
    solved_zero_row = solved.index(0) // size
    solved_zero_column = solved.index(0) % size
    taxicab = abs(puzzle_zero_row - solved_zero_row) + abs(puzzle_zero_column - solved_zero_column)

    gg = get_zero_sol(puzzle, size)

    if taxicab % 2 == 0 and res % 2 == 0:
        return True
    if taxicab % 2 == 1 and res % 2 == 1:
        return True
    return False

    return res % 2 == 0


def get_solved(size):
    sol = [[-1 for x in range(size)] for y in range(size)]
    move = [[0,1],[1,0],[0,-1],[-1,0]]
    index = 0
    fail = 0
    num = 1
    y = 0
    x = 0
    sol[y][x] = num
    num += 1
    while fail < 4:
        if y + move[index][0] >= size or y + move[index][0] < 0 or\
            x + move[index][1] >= size or x + move[index][1] < 0 or\
                sol[move[index][0] + y][move[index][1] + x] != -1:
            fail += 1
            index += 1
            if index >= 4:
                index = 0
        else:
            y += move[index][0]
            x += move[index][1]
            if size * size == num:
                sol[y][x] = 0
                break
            sol[y][x] = num
            num += 1
            fail = 0

    print(list(sum(sol, [])))
    return list(sum(sol, []))


def get_zero_sol(puzzle, size):
    res = 0
    temp = 0
    i = 0
    while i < len(puzzle):
        if puzzle[i] == 0:
            temp = i
            # print("res-temp: ", temp)
            break
        i += 1
    while temp > 0:
        temp -= size
        res += 1
    # print("res - zero: ", res)

    return res

# get_solved(3)
# get_solved(4)
# get_solved(5)
# get_solved(6)
# get_solved(7)
# print(is_solved([0, 2, 4, 1, 8, 5, 3, 6, 7]))  # unsolved
# print(is_solved([5, 8, 6, 7, 0, 2, 3, 4, 1]))  # get_solved
# print(is_solved([8, 1, 3, 4, 5, 2, 0, 7, 6]))  # get_solved
# print(is_solved([0, 3, 8, 1, 4, 7, 6, 5, 2]))  # get_solved
# print(is_solved([0, 8, 3, 5, 7, 1, 4, 6, 2]))  # unsolved
# print(is_solved([1, 8, 4, 2, 0, 7, 5, 3, 6]))  # unsolved
# 2, 3, 1, 6, 0, 4, 7, 5, 8