# 3. Реализовать склонение слова «процент» для чисел до 20. 
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». 
# Вывести все склонения для проверки.

case_1 = ''                                                                                         # запись окончания "процент" для числа 1
case_2_4 = 'а'                                                                                      # запись окончания "процент" для чисел от 2 до 4 включительно
case_5_20 = 'ов'                                                                                    # запись окончания "процент" для чисел от 5 до 20 включительно
checklist = []                                                                                      # создание списка для записи склонений с рядом чисел от 0 до 20 вкл.

user_number = int(input('Введите число от 0 до 20, а я просклоняю с ним слово "процент": '))

for n in range(21):
    if n == 1:
        checklist.append(str(n) + ' процент' + case_1)
    elif n > 1 and n < 5:
        checklist.append(str(n) + ' процент' + case_2_4)
    elif n >= 5 and n <= 20 or n == 0 :
        checklist.append(str(n) + ' процент' + case_5_20)
    print(checklist[n])                                                                              # вывести все склонения для проверки.

print('_' * 70, '\n')                                                                                # для читаемости вывода
print('С вашим числом слово "процент" склоняется вот так:', checklist[user_number])                  # вывод склонения "процент" для заданного пользователем числа
print('_' * 70)                                                                                      # для читаемости вывода

