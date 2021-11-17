from queue import PriorityQueue
from heapq import *
from typing import List, Tuple
from copy import deepcopy
import datetime




class Table:
    def __init__(self, map: List[List], zero_position: Tuple, prev: Tuple = None, path: int = 0):
        self.map = map
        self.prev = prev
        self.x, self.y = zero_position
        self.max_x = len(map)
        self.max_y = len(map[0])
        self.datetime = datetime.datetime.now()
        self.name = self._name()
        self.path = path

    def __str__(self):
        res = ''
        for line in self.map:
            for item in line:
                res += f"|{item}|"
            res += '\n'
        return res

    def __lt__(self, other):
        # return self.map < other.map
        return self.datetime < other.datetime

    def __gt__(self, other):
        # return self.map > other.map
        return self.datetime > other.datetime

    def _name(self):
        lst = list()
        for item in self.map:
            lst.extend(item)
        return tuple(lst)

    def get_neighbors(self):
        neibors = list()
        res = list()
        k = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in k:
            buf_x = self.x + x
            buf_y = self.y + y
            if buf_x < 0 or buf_x >= self.max_x or buf_y < 0 or buf_y >= self.max_y:
                continue
            neibors.append((buf_x, buf_y))
        for x, y in neibors:
            buf = deepcopy(self.map)
            temp = buf[x][y]
            buf[x][y] = 0
            buf[self.x][self.y] = temp
            test = Table(buf, (x, y), self.name, self.path + 1)
            res.append(test)
        return res

    def heuristic_man(self, coords: dict) -> int:
        res = 0
        for x, line in enumerate(self.map):
            for y, elem in enumerate(line):
                x1, y1 = coords[elem]
                res += abs(x1 - x) + abs(y1 - y)
        return res

    def equals(self, map: List[List]):
        return self.map == map


def search_item(map: List[List], item: int):
    for x, line in enumerate(map):
        for y, elem in enumerate(line):
            if elem == item:
                return x, y


def get_coords(x_max: int, y_max: int) -> dict:
    res = dict()

    def gen(x: int, y: int):
        num = 1
        max = x * y
        while num < max:
            yield num
            num += 1
        yield 0

    k = gen(x_max, y_max)
    for x in range(x_max):
        for y in range(y_max):
            res[next(k)] = tuple([x, y])
    return res


if __name__ == '__main__':

    # m = [[0, 2, 3],
    #      [4, 1, 6],
    #      [7, 8, 5]]
    #
    # m1 = [[4, 5, 6],
    #       [1, 2, 3],
    #       [7, 8, 0]]
    #
    # m2 = [[7, 8, 0],
    #       [1, 2, 3],
    #       [4, 5, 6]]
    #
    # m3 = [[1, 4, 3],
    #       [2, 7, 6],
    #       [5, 8, 0]]
    #
    # m4 = [[1, 2, 3],
    #       [4, 5, 6],
    #       [7, 8, 0]]
    #
    # test = Table(m, (0, 0))
    # test1 = Table(m1, (2, 2))
    # test2 = Table(m2, (0, 2))
    # test3 = Table(m3, (2, 2))
    # test4 = Table(m4, (2, 2))
    #
    # queue = []


    coords = get_coords(3, 3)

    m = [[4, 6, 7],
          [8, 0, 2],
          [5, 3, 1]]

    goal = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]
    #
    # der = [[1, 4, 8],
    #         [7, 3, 0],
    #         [6, 5, 2]]

    # new = Table(der, (1, 2))
    # ns = new.get_neighbors()
    root = Table(m, (1, 1))
    # print(root.name)
    # g = Table(goal, (2, 2))
    # print(g.name)
    closed = dict()
    pq = PriorityQueue()
    pq.put((root.heuristic_man(coords), root))
    while not pq.empty():
        idx, cur_node = pq.get()
        print(idx)
        if cur_node.equals(goal):
            print("got it")
            break

        nodes = cur_node.get_neighbors()
        for node in nodes:
            new_cost = node.path + node.heuristic_man(coords)
            if node.name not in closed:
                # closed[node.name].path = node.path
                pq.put((new_cost, node))
            if closed.get(node.name, None) is not None:
                if (closed[node.name].path + closed[node.name].heuristic_man(coords)) > new_cost:
                    closed[node.name].path = node.path
                    pq.put((new_cost, node))
    print("EBANA")
    # cost_visited = {root.name: 0}
    # visited = {root.name: None}
    # i = 0
    # while not pq.empty():
    #     cur_cost, cur_node = pq.get()
    #     print(cur_cost)
    #     if cur_node.equals(goal):
    #         print("resheno")
    #         print(visited)
    #         break
    #     nodes = cur_node.get_neighbors()
    #     for node in nodes:
    #         new_cost = node.path
    #         if node.name not in cost_visited or new_cost < cost_visited[node.name]:
    #             priority = new_cost + node.heuristic_man(coords)
    #             pq.put((priority, node))
    #             cost_visited[node.name] = new_cost
    #             visited[node.name] = cur_node.name
    #
    # print("NEHUA")
    #     i += 1
    #     id, current = pq.get()
    #     print(id)
    #     if current.name in closed.keys():
    #         continue
    #     if id == 6:
    #         print('hello')
    #     if current.equals(goal):
    #         print("RESHENO")
    #         print(closed)
    #         break
    #     closed[current.name] = current
    #     neighbors = current.get_neighbors()
    #     for node in neighbors:
    #         if node.name in closed.keys():
    #             continue
    #         idx = node.heuristic_man(coords)
    #         pq.put((idx, node))
    # print("IDI NAHUI MAFAKA")
    # for tst in [test, test1, test2, test3, test4]:
    #     buf = tst.heuristic_man(coords)
    #     print(buf)

    # k = search_item(m3, 0)
    # print(k)

    # print(test)
    # k = test.get_neighbors()
    # for i in k:
    #     print(type(i))
    #     print(i)

    # q.put((3, test2))
    # q.put((1, test3))
    # q.put((10, test))
    # q.put((3, test1))
    #
    # for i in range(5):
    #     if not q.empty():
    #         idx, tst = q.get()
    #         print(idx)
    #         print(type(tst))
    #         print(tst.name)
    #         print(tst)

    # print(q.get())
    # print(q.get())
    # print(q.get())
    # print(q.get())
    # print(q.empty())

    X = 3
    Y = 3
    # res = dict()
    # # lst = list()
    # #
    # # for x in range(X):
    # #     buf = [0 for y in range(Y)]
    # #     lst.append(buf)
    # #
    # # print(lst)
    #
    #
    # def gen(X, Y):
    #     num = 1
    #     max = X * Y
    #     while num < max:
    #         yield num
    #         num += 1
    #     yield 0
    #
    #
    # k = gen(X, Y)
    # for x in range(X):
    #     for y in range(Y):
    #         res[next(k)] = tuple([x, y])
            # lst[x][y] = next(k)


    # print(res)
