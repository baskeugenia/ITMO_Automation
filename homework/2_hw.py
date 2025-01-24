def task_1() -> tuple:
    a:int = 100
    b:float = 0.01
    c:str = '010'
    d:list = [0, 0, 1, 0, 0]
    e:bool = 0

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

    return a, b, c, d, e

x = task_1()
#print(type(x))


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21] # Fibonacci numbers / ряд Фибоначчи
    print(a[0:3])
    return a

task_2()
#print(task_2())


def task_3(x:float):
    return x**x

print(task_3(3)) # 27
print(task_3(0)) # 1
print(task_3(0.1)) # 0.7943282347242815


