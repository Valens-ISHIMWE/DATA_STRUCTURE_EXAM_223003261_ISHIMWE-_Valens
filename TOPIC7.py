# Min-Heap for Public Transport Scheduling
import heapq

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

def heap_sort(data):
    heapq.heapify(data)
    sorted_data = []
    while data:
        sorted_data.append(heapq.heappop(data))
    return sorted_data




print("\n=== Heap Sort ===")
routes = [(3, "Kigali_Huye"), (1, "Kigali_Muhanga"), (2, "Kigali_Nyanza")]
print("Unsorted Routes:", routes)
sorted_routes = heap_sort(routes)
print("Sorted Routes:", sorted_routes)

