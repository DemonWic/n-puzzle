import argparse
import sys
from npuzzle import a_star_search
from heuristics import get_heuristic
from solved_system import is_solved, get_solved
from visualizer import visualuzation


def validate_table(filename):
    size = 0
    res = []
    try:
        buf = []
        with open(filename, 'r') as f:
            for line in f:
                if "#" not in line:
                    buf.append(line.strip())

        if not (buf[0].isdecimal() and int(buf[0]) >= 0):
            raise Exception("Not valid start table: size not valid number")
        size = int(buf[0])
        for row in buf[1:]:
            for num in [x.strip() for x in row.split()]:
                if not (num.isdecimal() and int(num) >= 0):
                    raise Exception("Not valid start table: not valid number in table")
                res.append(int(num))

        if len(res) != size ** 2:
            raise Exception("Not valid start table: the size does not match the table")
        return True, size, res
    except Exception as e:
        print(str(e), file=sys.stderr)
        return False, size, res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="filename with start table")
    parser.add_argument("-g", "--graphic", help="on graphic mode", action="store_true")
    parser.add_argument("-H", "--heuristic", type=str, help="heuristic for algorithm, default - manhattan",
                        choices=['manhattan', 'hamming', 'linear'], default='manhattan')

    args = parser.parse_args()

    v_res, t_size, table = validate_table(args.filename)

    if is_solved(table, t_size, get_solved(t_size)):
        print("solvable")
    else:
        print("unsolvable")
        sys.exit(1)

    if not v_res:
        sys.exit(1)

    func = get_heuristic(args.heuristic)
    dst = get_solved(t_size)
    status, result, r_space, r_time = a_star_search(table, tuple(dst), t_size, func, 1)
    if not status:
        print("unsolvable")
    elif args.graphic:
        visualuzation(result, t_size)
    else:
        for x in result:
            print(x)
        print(f"space complexity: {r_space} nodes in memory")
        print(f"time complexity: {r_time} evaluated nodes")



