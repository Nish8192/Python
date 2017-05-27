class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def PrintAllVals(self):
        runner = self.head
        while(runner != None):
            print runner.value
            runner = runner.next

    def AddBack(self, value):
        runner = self.head
        new_node = Node(value)
        while(runner.next != None):
            runner = runner.next
        runner.add(new_node)

    def AddFront(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def InsertBefore(self, nextVal, value):
        new_node = Node(value)
        runner = self.head
        while(runner.next.value != nextVal):
            runner = runner.next
        new_node.add(runner.next)
        runner.add(new_node)

    def InsertAfter(self, preVal, value):
        new_node = Node(value)
        runner = self.head
        while(runner.value != preVal):
            runner = runner.next
        new_node.add(runner.next)
        runner.add(new_node)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, node):
        self.next = node


List = SinglyLinkedList()
List.head = Node('Alice')
List.head.next = Node('Chad')
List.head.next.next = Node('Debra')

# List.PrintAllVals()

List.AddBack('Nishant')
# List.PrintAllVals()

List.AddFront('Nishant')

# List.InsertBefore('Chad', 'Brian')

List.InsertAfter('Alice', 'Tim')
List.PrintAllVals()



 # something close to this should be utilized for all of the above problems
# runner = List.head
# while(runner.next != None):
#     print(runner.val)
#     runner = runner.next
