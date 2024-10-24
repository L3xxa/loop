from functions import count_digits, sum_digits,middle_arithmetic,zeros

a = int(input("Введіть число : "))
par = int(input("Виберіть функцію:\n"
                "1:Дізнатися к-ть чисел:\n"
                "2:Дізнатися суму чисел:\n"
                "3:Дізнатися середньоарифметичне:\n"
                "4:Дізнатися к-ть нулів:\n"
                "1-4: "))

result_count = count_digits(a)
result_sum = sum_digits(a)
result_mid = middle_arithmetic(a)
result_zero = zeros(a)

if par == 1:
    print (f'К-ть чисел = {result_count}')
elif par == 2:
    print(f'Сума чисел = {result_sum}')
elif par == 3 :
    print(f'Середньоарифметичне числа = {result_mid} ')
elif par == 4:
    print(f'К-ть нулів = {result_zero}')
