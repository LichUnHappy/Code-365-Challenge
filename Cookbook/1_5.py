# 实现一个优先级队列

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name 
    
    def __repr__(self) -> str:
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 6)
q.push(Item('spam'), 2)
q.push(Item('car'), 4)
q.push(Item('bat'), 3)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())