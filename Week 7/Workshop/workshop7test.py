import unittest
from workshop7 import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.myQueue = PriorityQueue()

    def test_init(self):
        self.assertEqual(len(self.myQueue.queue), 0)

    def test_isEmpty(self):
        self.assertTrue(self.myQueue.isEmpty(), "Priority queue is not empty")

    def test_add(self):
        self.myQueue.add(1,1)
        self.assertEqual(len(self.myQueue.queue), 1)

        self.myQueue.add(2,2)
        self.myQueue.add(3,3)
        self.myQueue.add(4,4)
        self.myQueue.add(5,5)
        self.assertEqual(len(self.myQueue.queue), 5)

    def test_pop(self):
        self.myQueue.add(1,1)
        pop = self.myQueue.pop()
        self.assertEqual(pop, 1)
        self.assertEqual(len(self.myQueue.queue), 0)

        self.myQueue.add(5,2)
        self.myQueue.add(4,3)
        self.myQueue.add(3,4)
        self.myQueue.add(2,5)
        pop = self.myQueue.pop()
        self.assertEqual(pop, 2)
        self.assertEqual(len(self.myQueue.queue), 3)

        pop = self.myQueue.pop()
        self.assertEqual(pop, 3)
        self.assertEqual(len(self.myQueue.queue), 2)

        pop = self.myQueue.pop()
        self.assertEqual(pop, 4)
        self.assertEqual(len(self.myQueue.queue), 1)

        pop = self.myQueue.pop()
        self.assertEqual(pop, 5)
        self.assertTrue(self.myQueue.isEmpty(), "Priority queue is not empty")

    def test_peep(self):
        self.myQueue.add(1,1)
        peep = self.myQueue.peep()
        self.assertEqual(peep, 1)
        self.assertEqual(len(self.myQueue.queue), 1)

        self.myQueue.add(10, 2)
        self.myQueue.add(9, 3)
        self.myQueue.add(3, 4)
        self.myQueue.add(2, 5)
        peep = self.myQueue.peep()
        self.assertEqual(peep, 2)
        self.assertEqual(len(self.myQueue.queue), 5)


if __name__ == '__main__':
    unittest.main()
