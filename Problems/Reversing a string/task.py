from collections import deque
n = int(input())

my_stack = deque()

for a in range(n):
    my_stack.append(input())

for a in range(n):
    print(my_stack.pop())
