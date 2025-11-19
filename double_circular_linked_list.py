dll = DoublyCircularLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

dll.prepend(5)          # [5,10,20,30]
dll.insert(2, 15)       # [5,10,15,20,30]

print(dll)
# 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> (back to head)

dll.remove(20)
print(dll)
# 5 <-> 10 <-> 15 <-> 30 <-> (back to head)

print(dll.find(15))
# Node(15)
