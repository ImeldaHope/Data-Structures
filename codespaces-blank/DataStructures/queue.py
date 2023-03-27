"""
Implementing a queue below.
"""
#import deque
from collections import deque

my_queue = deque()

#add data to the queue
my_queue.append(100)
my_queue.append(200)
my_queue.append(300)
my_queue.append(400)
my_queue.append(500)

#preview queue content
print(my_queue)

#remove value from queue using FIFO. This will show value that has been removed.
print(my_queue.popleft())

#preview queue content to show remain values.
print(my_queue)
