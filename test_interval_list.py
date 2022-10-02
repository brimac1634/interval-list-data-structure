import unittest
from interval_list import IntervalList

class TestIntervalList(unittest.TestCase):
    
    def test_add_and_remove(self):
        """
        Tests add and remove methods sequentially as outlined in assignment
        """
        
        rl = IntervalList()
        rl.add([1,5])
        self.assertEqual(rl.intervals, [[1,5]])
        rl.print()

        rl.add([10,20])
        self.assertEqual(rl.intervals, [[1,5], [10,20]])
        rl.print()

        rl.add([20,20])
        self.assertEqual(rl.intervals, [[1,5], [10,20]])
        rl.print()

        rl.add([20,21])
        self.assertEqual(rl.intervals, [[1,5], [10,21]])
        rl.print()

        rl.add([2,4])
        self.assertEqual(rl.intervals, [[1,5], [10,21]])
        rl.print()

        rl.add([3,8])
        self.assertEqual(rl.intervals, [[1,8], [10,21]])
        rl.print()

        rl.remove([10,10])
        self.assertEqual(rl.intervals, [[1,8], [10,21]])
        rl.print()

        rl.remove([10,11])
        self.assertEqual(rl.intervals, [[1,8], [11,21]])
        rl.print()

        rl.remove([15,17])
        self.assertEqual(rl.intervals, [[1,8], [11,15], [17,21]])
        rl.print()

        rl.remove([3,19])
        self.assertEqual(rl.intervals, [[1,3], [19,21]])
        rl.print()


    def test_operators(self):
        """
        Tests operator overrides as outlined in assignment
        """

        ra = IntervalList();
        ra.add([1, 5]);

        rb = IntervalList();
        rb.add([1, 6]);

        self.assertEqual(ra > rb, False)
        print(ra > rb)

        self.assertEqual(ra < rb, True)
        print(ra < rb)

        self.assertEqual(ra >= rb, False)
        print(ra >= rb)

        self.assertEqual(ra <= rb, True)
        print(ra <= rb)

        self.assertEqual(ra == rb, False)
        print(ra == rb)

        self.assertEqual(ra in rb, True)
        print(ra in rb)


if __name__ == '__main__':
    unittest.main()
