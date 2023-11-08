# Simple list operations

# Create a list
my_list = [1, 2, 3, 4, 5]

# Append an element to the end of the list
my_list.append(6)

# Insert an element at a specific index
my_list.insert(0, 0)

# Remove an element from the end of the list
my_list.pop()

# Remove an element from a specific index
my_list.pop(0)

# Remove an element by value
my_list.remove(3)

# Get the length of the list
length = len(my_list)

# Get the index of an element
index = my_list.index(5)

# Check if an element is in the list
if 5 in my_list:
    print("5 is in the list")

# Iterate over the list
for element in my_list:
    print(element)

# Iterate over the list with index
for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")

# Iterate over the list with index and starting index
for index, element in enumerate(my_list, start=1):
    print(f"Index: {index}, Element: {element}")

# Sort the list
my_list.sort()

# Reverse the list
my_list.reverse()

# Clear the list
my_list.clear()




# Queue implementation using list

# Create a queue
queue = []

# Add elements to the queue
queue.append(1)

# Pop an element from the queue
queue.pop(0)

# Check if queue is empty
if not queue:
    print("Queue is empty")



# Stack implementation using list

# Create a stack
stack = []

# Add elements to the stack
stack.append(1)

# Pop an element from the stack
stack.pop()

# Check if stack is empty
if not stack:
    print("Stack is empty")


