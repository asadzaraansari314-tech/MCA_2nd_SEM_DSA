# linked list object class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

temp = first
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")