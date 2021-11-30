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
            i2 += 1
        i += 1

    src_zero_row = puzzle.index(0) // size
    src_zero_column = puzzle.index(0) % size
    dst_zero_row = solved.index(0) // size
    dst_zero_column = solved.index(0) % size
    cab = abs(src_zero_row - dst_zero_row) + abs(src_zero_column - dst_zero_column)

    if cab % 2 == 0 and res % 2 == 0:
        return True
    if cab % 2 == 1 and res % 2 == 1:
        return True
    return False


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

    return list(sum(sol, []))

