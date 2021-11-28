from copy import copy
from heapq import heappop, heappush
from itertools import count
import datetime
from queue import PriorityQueue

m = [[4, 6, 7],
          [8, 0, 2],
          [5, 3, 1]]

goal = [[1, 2, 3],
      [8, 0, 4],
      [7, 6, 5]]


# This puzzle is solvable
# 4
#  8  2  7  3
# 15  6  0  1
# 11 10  9  4
# 12  5 14 13


def get_neighbors(table, size, index):
    res = []
    indexes = [size, -size]
    if index % size != size - 1:
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

def manhattan2(candidate, solved, size):
    res = 0
    for i in range(size*size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            ci = solved.index(candidate[i])
            y = (i // size) - (ci // size)
            x = (i % size) - (ci % size)
            res += abs(y) + abs(x)
    return res

if __name__ == '__main__':

    # src = [4, 6, 7, 8, 0, 2, 5, 3, 1]
    # src = [4, 1, 2, 8, 0, 5, 6, 3, 7]
    # src = [11, 14,  9, 13, 10,  7,  0,  5, 2, 15, 6, 12, 3,  1,  8,  4]
    src = [8, 2, 7, 3,
           15, 6, 0, 1,
           11, 10, 9, 4,
           12, 5, 14, 13]
    # src = (8, 2, 7, 3, 15, 0, 6, 1, 11, 10, 9, 4, 12, 5, 14, 13)
    # src = (8, 2, 7, 3, 15, 6, 9, 1, 11, 10, 0, 4, 12, 5, 14, 13)
    # src = (8, 2, 7, 3, 15, 0, 6, 1, 11, 10, 9, 4, 12, 5, 14, 13)
    dst = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # dst2 = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    dst2 = (1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7)
    res = get_coords(src, 4)
    res2 = get_coords(dst, 3)
    res3 = get_coords(dst2, 4)
    # for num, coord in res.items():
    #     print(f"{num} {coord}")
    # print(">>>>>>>>>")
    # for num, coord in res2.items():
    #     print(f"{num} {coord}")

    # dist = manhattan(res, res3)
    # print(dist)
    # dist2 = manhattan2(src, dst2, 4)
    # print(dist2)
    # res = get_neighbors(src, 4, 6)
    # print(res)
    # for table, _ in res:
    #     for idx, num in enumerate(table):
    #         if idx % 4 == 0:
    #             print('\n')
    #         print(num, end=' ')
    #     print("\n>>>>>>>>>\n")


    # countt = count()
    start = datetime.datetime.now()
    queue = [(0, (tuple(src), 6), 0, None)]
    open_set = {}
    closed = {}
    cost = 1
    size = 4
    # i = 0
    goal_coord = get_coords(dst2, size)
    while queue:
        g, node_ind, node_w, parent = heappop(queue)
        # i += 1
        # print(i)
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
            break
        if node in closed:
            continue
        closed[node] = parent
        # with open('log.log', 'a') as f:
        #     f.write(f"g = {g}, c = {c}, node = {node}\n")
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
            heappush(queue, (next_w + neigh_h, (neighbor, n_idx), next_w, node))

    end = datetime.datetime.now()
    print(end - start)
    print("VSE GOVNO")


