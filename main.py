from function import function1, function2, function3
par = int(input("Виберіть рівень складності: \n"
                "1: Програма 1-го класу: \n"
                "2: Програма 7-го класу: \n"
                "3: Вища математика: \n"
                "Ваш вибір=>"))
if par == 1:
    function1()
elif par == 2:
    function2()
elif par == 3:
    function3()
else:
    print("Йой, я так не робив, дивись на варіанти")