# Second algorithm implementation: Priority queue

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, data):
        self.queue.append(data)
        if len(self.queue) > 3:
            self.pop()

    def pop(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i]['score'] < self.queue[min]['score']:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print('Cannot pop, queue is empty!')
