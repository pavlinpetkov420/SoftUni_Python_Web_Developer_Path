"""LISTS AS STACKS"""
# stack is LIFO linear structure of data
# LIFO - last in, first out
# diff between stacks and lists
# 00 - stack have less possibilities
# 01 - append and pop, item[-1], len are used operations
# TODO to check all information about stacks and queues as lists !!!

st = []

st.append(1)
st.append(-1)
st.append(55)
st.append(3)

while st:
    print(st.pop())

# Example class for stack
# class Stack:
#     def __init__(self):
#         self.internal_stack = []
#
#     def push(self, value):
#         self.internal_stack.append(value)
#
#     def pop(self):
#         return self.internal_stack.pop(eval())
#
#     def peek(self):
#         return self.internal_stack[-1]

# array list in python ???

"""LISTS AS QUEUES"""
# linear data structure
# FIFO - first in, first out
# enqueue -> append , dequeue -> popleft

from collections import deque

q = deque()
s = []

for i in range(1, 6):
    q.append(i)
    s.append(i)

print("Queue:")
while q:
    print(q.popleft())

print("Stack:")
while s:
    print(s.pop())


