from copy import copy
from heapq import heappop, heappush
from itertools import count

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
        res.append((tuple(buf), new))
    return res


def get_coords(lst, size):
    res = {}
    for idx, num in enumerate(lst):
        x = idx % size
        y = idx // size
        res[num] = (x, y)
    return res


def manhattan(src: dict, dst: dict):
    res = 0
    for num, coords in src.items():
        if num == 0:
            continue
        x, y = coords
        x1, y1 = dst[num]
        res += abs(x1 - x) + abs(y1 - y)
    return res


if __name__ == '__main__':

    src = [4, 6, 7, 8, 0, 2, 5, 3, 1]
    dst = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    dst2 = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    res = get_coords(src, 3)
    res2 = get_coords(dst, 3)
    res3 = get_coords(dst2, 3)
    # for num, coord in res.items():
    #     print(f"{num} {coord}")
    # print(">>>>>>>>>")
    # for num, coord in res2.items():
    #     print(f"{num} {coord}")

    # dist = manhattan(res, res2)
    # print(dist)
    # dist2 = manhattan(res, res3)
    # print(dist2)
    countt = count()
    queue = [(0, next(countt), (tuple(src), 4), 0, None)]
    open_set = {}
    closed = {}
    cost = 1
    size = 3
    goal_coord = get_coords(dst2, size)
    while queue:
        g, c, node_ind, node_w, parent = heappop(queue)
        node, idx = node_ind
        if node == dst2:
            print("NAIDENO!")
            res = [node]
            while parent is not None:
                res.append(parent)
                parent = closed[parent]
            res.reverse()
            print(len(res))
            for x in res:
                print(x)
        if node in closed:
            continue
        closed[node] = parent
        with open('log.log', 'a') as f:
            f.write(f"g = {g}, c = {c}, node = {node}\n")
        next_w = node_w + cost
        neighbors = get_neighbors(node, size, idx)
        for neighbor, n_idx in neighbors:
            if neighbor in closed:
                continue
            if neighbor in open_set:
                neigh_w, neigh_h = open_set[neighbor]
                if neigh_w <= next_w:
                    continue
            else:
                neigh_h = manhattan(get_coords(neighbor, size), goal_coord)

            open_set[neighbor] = next_w, neigh_h
            heappush(queue, (next_w + neigh_h, next(countt), (neighbor, n_idx), next_w, node))
    print("VSE GOVNO")

