import argparse
import sys

from solved_system import is_solved, get_solved


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
	parser.add_argument("-H", "--heuristic", type=str, help="heuristic for algorithm, default - manhattan",
						choices=['manhattan', 'hamming', 'linear'], default='manhattan')

	args = parser.parse_args()

	v_res, t_size, table = validate_table(args.filename)

	print(table)

	if is_solved(table, t_size, get_solved(t_size)):
		print("solved")
	else:
		print("unsolved")

	if not v_res:
		sys.exit(1)
