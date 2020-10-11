# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def add(self, priority, item):
        self.queue.append((priority, item))

    # for popping an element based on Priority
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] > self.queue[max][0]:
                    max = i
            item = self.queue[max][1]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    def peep(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] > self.queue[max][0]:
                    max = i
            item = self.queue[max][1]
            return item
        except IndexError:
            print()
            exit()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.add(12,12)
    myQueue.add(1,1)
    myQueue.add(14,14)
    myQueue.add(7,7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.pop())