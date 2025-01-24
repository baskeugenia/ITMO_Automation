
num = 3
num = 0
num = -0
num = -3

if num >= 0:
    print('Number is positive or 0')
else:
    print('Number is negaive')

str1 = 'some string'
str2 = 'some'

# contains?
# str2 in str1
if str1.find(str2) > -1:
    print('ДА')
else:
    print('НЕТ')


if num > 0:
    print('Number is positive')
elif num == 0:
    print('Number is 0')
else:
    print('Number is negaive')


def student_rank(c_num):
    if c_num in range(1, 5):
        print("Bachelor")
    elif c_num in range(5, 7):
        print("Master")
    elif c_num in range(7, 10):
        print("Doctor")
    else:
        print("Input correct year number")

student_rank(8)


def num_func(n):
    print('-' if n < -100 or n > 100 else '+')

num_func(0)
num_func(-99)
num_func(-100)
num_func(-101)
num_func(0)
num_func(100)
num_func(99)
num_func(101)