import heapq

# Circular Queue for Public Transport Scheduling
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return
        removed_data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_data

    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return
        index = self.front
        print("Circular Queue:", end=" ")
        while True:
            print(self.queue[index])
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print()

# Min-Heap for Public Transport Scheduling
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        heapq.heappush(self.heap, data)

    def remove(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return "Heap is Empty!"

    def display(self):
        print("Heap:", self.heap)



if __name__ == "__main__":
    # Circular Queue
    print("=== Circular Queue ===")
    cq = CircularQueue(5)
    cq.enqueue({"Agency":"volcano","From":"Kigali","To":"Muhanga"})
    cq.enqueue({"Agency":"Horizon","From":"Kigali","To":"Nyanza"})
    cq.enqueue({"Agency":"Stella","From":"Kigali","To":"Huye"})
    cq.display()
    print("Dequeued:", cq.dequeue())
    cq.display()

# Min Heap
print("\n=== Min Heap ===")
heap = MinHeap()
heap.insert((3, "Rwanda Air A"))
heap.insert((1, "Rwanda Air B"))
heap.insert((2, "Rwanda Air C"))
heap.display()
print("Removed:", heap.remove())
heap.display()