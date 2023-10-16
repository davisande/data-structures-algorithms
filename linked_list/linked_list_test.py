from linked_list import LinkedList


def new_linked_list():
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    return linked_list


numbers = new_linked_list()
print(numbers)

print('------APPEND-------')
numbers.append(2)
print(numbers)

print('-------APPEND------')
numbers.append(3)
print(numbers)

print('-------POP------')
numbers = new_linked_list()
numbers.pop()
print(numbers)

print('------POP-------')
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()

print('------PREPEND-------')
numbers = new_linked_list()
numbers.prepend(1)
print(numbers)

print('------PREPEND-------')
numbers.prepend(2)
print(numbers)

print('------PREPEND-------')
numbers.prepend(3)
numbers.prepend(4)
print(numbers)

print('------POP FIRST-------')
numbers = new_linked_list()
numbers.pop_first()
print(numbers)

print('------POP FIRST-------')
numbers.pop_first()
numbers.pop_first()
print(numbers)
numbers.pop_first()
print(numbers)
numbers.pop_first()
print(numbers)

print('------GET-------')
numbers = new_linked_list()
print(numbers.get(6))
print(numbers.get(0))
print(numbers.get(3))
print(numbers.get(4))

print('------SET-------')
numbers = new_linked_list()
numbers.set(0, 6)
print(numbers)
numbers.set(2, 7)
print(numbers)

print('------INSERT-------')
numbers = new_linked_list()
numbers.insert(0, 5)
print(numbers)
numbers.insert(2, 6)
print(numbers)
numbers.insert(6, 7)
print(numbers)

print('------REMOVE-------')
numbers = new_linked_list()
numbers.remove(4)
print(numbers)
numbers.remove(0)
print(numbers)
numbers.remove(1)
print(numbers)

print('------REVERSE-------')
numbers = new_linked_list()
numbers.reverse()
print(numbers)
