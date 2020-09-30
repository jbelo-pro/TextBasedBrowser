def range_sum(numbers, a, b):
    s = 0
    for x in numbers:
        if a <= x <= b:
            s += x
    return s


numbers = [int(x) for x in input().split()]
a, b =  input().split()
print(range_sum(numbers, int(a), int(b)))