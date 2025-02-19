
# Singly Linked List Implementation in Python
This code defines a Singly Linked List, where each node stores data and a reference to the next node. The Node class represents each element in the list, holding the data and a pointer (next) to the next node. The LinkedList class manages the list, starting with an empty list (head is None). The insert() method adds a new node at the beginning of the list, pushing the existing nodes one step further down. The display() method prints the list from the head node, showing the data of each node followed by an arrow (->), and ends with "None" to indicate the list's end.

# Doubly Linked List Implementation in Python
This code creates a Doubly Linked List, a data structure where each node contains data and references to both the next and previous nodes. The Node class stores the data and pointers to the next and previous nodes. The DoublyLinkedList class manages the list and allows you to add new nodes at the beginning using the insert() method. When you call insert(), the new node is added before the current head of the list. The display() method shows the list of elements in order, separated by "->", with "None" at the end to mark the end of the list.

# Circular Linked List Implementation in Python
This code implements a Circular Linked List, where each node points to the next node in the list, and the last node points back to the first node, forming a loop. The Node class stores the data and a reference to the next node. In the CircularLinkedList class, the insert() method adds a new node to the list, ensuring that the last node points back to the head to maintain the circular structure. The display() method traverses the list, printing the data of each node until it loops back to the head, indicating the circular nature of the list. The example usage shows how to insert nodes and display the circular list, which will print each element in a loop, ending with "Back to Head."

# Graph Implementation in Python
This code defines a graph using a dictionary, where each key represents a node, and the value is a list of nodes that the key node is connected to. For example, the node 'vowel' is connected to 'a' and 'e', and the node 'number' is connected to '1' and '2'. The display_graph() function iterates through each node in the graph and prints the node followed by the list of its connections (neighbors). The output will display each node and its associated connections, showing how the graph is structured. Finally, the display_graph(graph) call prints the graph's structure to the console.

# Heap Implementation in Python
This code demonstrates the use of a min-heap with Python's heapq module. A min-heap is a binary heap where the smallest element is always at the root. The heappush() function adds elements to the heap, maintaining the heap property. In this example, the numbers 2, 1, and 3 are pushed into the heap, and they will be arranged such that the smallest element is at the top. The heappop() function removes and returns the smallest element from the heap, so the output will first print 1, then 2, showing the order in which the elements are removed.

# Queue Implementation in Python
This code demonstrates the use of a queue using the deque class from Python's collections module. A deque (double-ended queue) allows efficient appending and popping of elements from both ends. The append() method adds elements to the right end of the queue. The popleft() method removes and returns elements from the left end, following the first-in-first-out (FIFO) principle. In this example, the numbers 1, 2, and 3 are added to the queue, and the first two elements (1 and 2) are removed and printed using popleft().

# Stack Implementation in Python
This code demonstrates the use of a stack in Python, implemented using a list. A stack follows the last-in, first-out (LIFO) principle, meaning the last element added is the first one to be removed. The append() method adds elements to the top of the stack. The pop() method removes and returns the top element of the stack. In this example, the numbers 1, 2, and 3 are added to the stack, and the last two elements (3 and 2) are removed and printed using pop().

# Trees Implementation in Python
This code implements an in-order traversal of a binary tree. The Node class represents each node of the tree, storing the node's data and pointers to its left and right child nodes. The inorder() function recursively visits the left subtree, prints the current node's data, and then visits the right subtree. The tree is structured with the root node having data 2, with left and right children 3 and 5, respectively. When calling inorder(root), it prints the nodes in ascending order: 6 3 7 2 5, following the in-order traversal pattern (left, root, right).
