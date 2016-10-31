#square = lambda x: x ** 2
#for val in map(square, range(1, 20)):
#    print(val, end=' ')


#is_even = lambda x: x % 2 == 0
#for val in filter(is_even, range(10)):
#    print(val, end=' ')

from itertools import combinations
c = combinations(range(1, 5), 3)
print(*c)
