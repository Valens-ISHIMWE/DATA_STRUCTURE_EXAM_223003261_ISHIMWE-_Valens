# Doubly Linked List for Dynamic Tracking
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display_forward(self):
        temp = self.head
        print("Forward:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print()

print("\n=== Doubly Linked List ===")
dll = DoublyLinkedList()
dll.append("Muhanga public Parking")
dll.append("Nyanza public Parking")
dll.append("Huye public Parking")

dll.display_forward()
