def greater(n1:float, n2:float):
    print(n1 if n1 > n2 else n2)
    #или max(n1, n2)

greater(1, 200)
greater(100, -100)
greater(0,0)


def dif135(n1:float, n2:float):
    print('yes' if abs(n1-n2) == 135 else 'no')

dif135(0, 135)
dif135(135, 0)
dif135(1,2)


def season(n:int):
    if n == 12 or n == 1 or n == 2:
        print("зима")
    elif n in (3, 6):
        print("весна")
    elif n in (6, 9):
        print("лето")
    elif n in (9, 12):
        print("осень")
    else:
        print("введите число месяца")

season(12)
season(1)
season(112)


def greater_10(n1:float, n2:float, n3:float):
    print('yes' if n1 > 10 and n2 > 10 and n3 > 10 else 'no')

greater_10(11, 11, 11)
greater_10(10, 11, 11)
greater_10(0, 2, 3)


def num_pos(l:list) -> int:
    x = 0
    for n in l:
        if n > 0:
            x += 1
    print(x)
    return x

num_pos([1, -1, 2, -2, 0])


def num_days(y:int, m:int):
    print((y * 12 + m) * 29)

num_days(0, 0)
num_days(0, 1)
num_days(1, 0)
num_days(1, 1)
num_days(10, 10)