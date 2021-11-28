import unittest
from npuzzle import get_neighbors


class Test_get_neighbors(unittest.TestCase):

    def test_1(self):
        in_table = tuple((4, 6, 7, 8, 0, 2, 5, 3, 1))
        out = (((4, 6, 7, 0, 8, 2, 5, 3, 1), 3),
               ((4, 6, 7, 8, 2, 0, 5, 3, 1), 5),
               ((4, 0, 7, 8, 6, 2, 5, 3, 1), 1),
               ((4, 6, 7, 8, 3, 2, 5, 0, 1), 7))
        res = get_neighbors(in_table, 3, 4)
        self.assertEqual(len(out), len(res), "Not equal count result")
        for r in res:
            self.assertIn(r, out)

    def test_2(self):
        in_table = tuple((4, 6, 7, 8, 1, 2, 5, 3, 0))
        out = (((4, 6, 7, 8, 1, 2, 5, 0, 3), 7),
               ((4, 6, 7, 8, 1, 0, 5, 3, 2), 5))
        res = get_neighbors(in_table, 3, 8)
        self.assertEqual(len(out), len(res), "Not equal count result")
        for r in res:
            self.assertIn(r, out)

    def test_3(self):
        in_table = tuple((0, 6, 7, 8, 1, 2, 5, 3, 4))
        out = (((6, 0, 7, 8, 1, 2, 5, 3, 4), 1),
               ((8, 6, 7, 0, 1, 2, 5, 3, 4), 3))
        res = get_neighbors(in_table, 3, 0)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)

    def test_4(self):
        in_table = tuple((7, 6, 0, 8, 1, 2, 5, 3, 4))
        out = (((7, 0, 6, 8, 1, 2, 5, 3, 4), 1),
               ((7, 6, 2, 8, 1, 0, 5, 3, 4), 5))
        res = get_neighbors(in_table, 3, 2)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)

    def test_5(self):
        in_table = tuple((7, 6, 2, 8, 1, 0, 5, 3, 4))
        out = (((7, 6, 2, 8, 0, 1, 5, 3, 4), 4),
               ((7, 6, 2, 8, 1, 4, 5, 3, 0), 8),
               ((7, 6, 0, 8, 1, 2, 5, 3, 4), 2))
        res = get_neighbors(in_table, 3, 5)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)

    def test_6(self):
        in_table = tuple((7, 0, 2, 8, 1, 6, 5, 3, 4))
        out = (((0, 7, 2, 8, 1, 6, 5, 3, 4), 0),
               ((7, 2, 0, 8, 1, 6, 5, 3, 4), 2),
               ((7, 1, 2, 8, 0, 6, 5, 3, 4), 4))
        res = get_neighbors(in_table, 3, 1)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)

    def test_7(self):
        in_table = tuple((7, 8, 2, 0, 1, 6, 5, 3, 4))
        out = (((0, 8, 2, 7, 1, 6, 5, 3, 4), 0),
               ((7, 8, 2, 1, 0, 6, 5, 3, 4), 4),
               ((7, 8, 2, 5, 1, 6, 0, 3, 4), 6))
        res = get_neighbors(in_table, 3, 3)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)

    def test_8(self):
        in_table = tuple((7, 8, 2, 5, 1, 6, 0, 3, 4))
        out = (((7, 8, 2, 0, 1, 6, 5, 3, 4), 3),
               ((7, 8, 2, 5, 1, 6, 3, 0, 4), 7))
        res = get_neighbors(in_table, 3, 6)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)

    def test_9(self):
        in_table = tuple((7, 8, 2, 5, 1, 6, 3, 0, 4))
        out = (((7, 8, 2, 5, 0, 6, 3, 1, 4), 4),
               ((7, 8, 2, 5, 1, 6, 0, 3, 4), 6),
               ((7, 8, 2, 5, 1, 6, 3, 4, 0), 8))
        res = get_neighbors(in_table, 3, 7)
        self.assertEqual(len(out), len(res))
        for r in res:
            self.assertIn(r, out)



if __name__ == '__main__':
    unittest.main()
