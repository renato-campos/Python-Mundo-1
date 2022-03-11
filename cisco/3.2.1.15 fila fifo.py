class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__fila = []


    def put(self, elem):
        self.__fila.append(elem)


    def get(self):
        elem = self.__fila[0]
        del self.__fila[0]
        return elem


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
'''
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

'''