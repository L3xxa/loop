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
