from copy import copy


m = [[4, 6, 7],
          [8, 0, 2],
          [5, 3, 1]]

goal = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 0]]


def get_neighbors(table, size, index):
    res = []
    indexes = [size, -size]
    if index % size != 2:
        indexes.append(1)
    if index % size != 0:
        indexes.append(-1)
    for idx in indexes:
        new = idx + index
        if new < 0 or new >= size ** 2:
            continue
        buf = copy(list(table))
        temp = buf[new]
        buf[new] = buf[index]
        buf[index] = temp
        res.append((buf, new))
    return res
