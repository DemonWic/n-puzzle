from copy import deepcopy


def manhattan(src: dict, dst: dict, size: int) -> int:
    res = 0
    for num, coords in src.items():
        if num == 0:
            continue
        x, y = coords
        x1, y1 = dst[num]
        res += abs(x1 - x) + abs(y1 - y)
    return res


def hamming(src: dict, dst: dict, size: int) -> int:
    res = 0
    for num, coords in src.items():
        if num != 0 and dst[num] != coords:
            res += 1
    return res


def linear(src: dict, dst: dict, size: int) -> int:

    def conflict_count(candidate_row, solved_row, size, ans=0):
        counts = [0 for x in range(size)]
        for i, num1 in enumerate(candidate_row):
            if num1 in solved_row and num1 != 0:
                for j, num2 in enumerate(candidate_row):
                    if num2 in solved_row and num2 != 0:
                        if num1 != num2:
                            if (solved_row.index(num1) > solved_row.index(num2)) and i < j:
                                counts[i] += 1
                            if (solved_row.index(num1) < solved_row.index(num2)) and i > j:
                                counts[i] += 1
        if max(counts) == 0:
            return ans * 2
        else:
            i = counts.index(max(counts))
            candidate_row[i] = -1
            ans += 1
            return conflict_count(candidate_row, solved_row, size, ans)

    res = manhattan(src, dst)
    buf = [0 for x in range(size)]
    src_rows = [deepcopy(buf) for y in range(size)]
    src_columns = [deepcopy(buf) for x in range(size)]
    dst_rows = [deepcopy(buf) for y in range(size)]
    dst_columns = [deepcopy(buf) for x in range(size)]
    for num, x_y in src.items():
        x, y = x_y
        src_rows[y][x] = num
        src_columns[x][y] = num
    for num, x_y in dst.items():
        x, y = x_y
        dst_rows[y][x] = num
        dst_columns[x][y] = num
    for i in range(size):
        res += conflict_count(src_rows[i], dst_rows[i], size)
        res += conflict_count(src_columns[i], dst_columns[i], size)

    return res


def get_heuristic(name: str):
    return eval(name)
