from collections import deque
operations = int(input())

my_stack = deque()
for n in range(operations):
    op = input().split()
    if 'PUSH' in op:
        my_stack.append(op[1])
    else:
        my_stack.pop()

for n in range(len(my_stack)):
    print(my_stack.pop())

