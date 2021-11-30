from copy import copy
from heapq import heappop, heappush
import datetime


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


def a_star_search(src: list, dst: tuple, size: int, heuristic, cost: int = 1):
    start = datetime.datetime.now()
    queue = [(0, (tuple(src), src.index(0)), 0, None)]
    opened = {}
    closed = {}
    goal_coord = get_coords(dst, size)
    while queue:
        g, node_ind, node_w, parent = heappop(queue)
        node, idx = node_ind
        if node == dst:
            res = [node]
            while parent is not None:
                res.append(parent)
                parent = closed[parent]
            res.reverse()
            # end = datetime.datetime.now()
            # print(end - start)
            return True, res, len(opened), len(closed)
        if node in closed:
            continue
        closed[node] = parent
        next_w = node_w + cost
        neighbors = get_neighbors(node, size, idx)
        for neighbor, n_idx in neighbors:
            if neighbor in closed:
                continue
            if neighbor in opened:
                neigh_w, neigh_h = opened[neighbor]
                if neigh_w <= next_w:
                    continue
            else:
                neigh_h = heuristic(get_coords(neighbor, size), goal_coord, size)

            opened[neighbor] = next_w, neigh_h
            heappush(queue, (next_w + neigh_h, (neighbor, n_idx), next_w, node))

    # end = datetime.datetime.now()
    # print(end - start)
    return False, [], len(opened), len(closed)
