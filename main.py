from functions import count_digits, sum_digits

a = int(input("Введіть число : "))
par = int(input("Виберіть функцію:\n"
                "1:Дізнатися кількість чисел:\n"
                "2:Дізнатися суму чисел:\n"
                "1-2: "))

result_count = count_digits(a)
result_sum = sum_digits(a)

if par == 1:
    print (f'Кількість чисел = {result_count}')
elif par == 2:
    print(f'Сума чисел = {result_sum}')





