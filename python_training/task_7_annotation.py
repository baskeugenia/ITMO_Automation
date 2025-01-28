
a: int = 5
b: str = 'string'
c: list = (1,2,3)

def square(s: str, width:int) -> int:
    return " " * (max(0, width - len(s))) + s


print(square('str', 5))

def str_len(s:str='') -> int:
    return len(s)

print(str_len('some str'))
print(str_len())


def two_lists(a:list, b:list) -> int:
    return max(len(a), len(b))


print(two_lists([1, 2, 3], [4, 5, 6, 7, 8]))


def list_rnd(l:list) -> list:
    l.append('rnd')
    return l

print(list_rnd(['l', 'i', 's', 't']))

def l_sum(x:list[int]) -> int:
    return sum(x)

print(l_sum([0, 10, 20, 30]))
print(l_sum([1, 2, 3, 4]))