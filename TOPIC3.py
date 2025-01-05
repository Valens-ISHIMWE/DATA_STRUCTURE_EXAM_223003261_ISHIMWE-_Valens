# Linked List for Scheduling Processing
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = LinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

print("\n=== Linked List ===")
ll = LinkedList()
ll.append("Kivu belt bus: Schedule 8:00 AM")
ll.append("Ritico bus: Schedule 9:00 AM")
ll.display()