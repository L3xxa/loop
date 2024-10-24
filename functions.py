def count_digits (num):
    count = 0
    for i in str(num):
        count += 1
    return count


def sum_digits (num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

def middle_arithmetic (num):
    mid = 0
    count = 0
    for i in str(num):
        mid += int(i)
        count += 1

    if count == 0:
        return 0
    middle = mid/count
    return middle


def zeros (num):
    zer = 0
    for i in str(num):
        if i == '0':
            zer += 1
    return zer



