# *(вместо задачи 3) Написать функцию thesaurus_adv(), 
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, 
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     }, 
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"], 
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args):
    # создаем пустой словарь
    names_dict = {}
    # передаем аргументы вызова функции в пустой список
    names_list = list(args)

    #итерируем сразу отсортированный список с аргументами для сортировки ключей второго уровня
    for i in sorted(names_list):
        # каждый элемент списка бьется на два списка, достается второй элемент (фамилия) в новом списке и возвращается его первая буква
        first_surname_letter = i.split(' ')[-1:][0][0]
        # записываем первую букву фамилии в словарь первого уровня
        # записываем первую букву имени в словарь второго уровня
        # в значения словарей второго уровня записываем список
        names_dict.setdefault(first_surname_letter, {}).setdefault(i[0],[])
        # вызываем список из значений словарей второго уровня и
        # записываем значения в списки
        names_dict[first_surname_letter][i[0]].append(i)
    # сортируем ключи первого уровня
    return dict(sorted(names_dict.items()))


print(thesaurus_adv("Иван Сергеев", "Петр Алексеев", 'Кантемир Савоськин', "Инна Серова", "Илья Иванов", "Анна Савельева", 'Ираклий Ибрашидзе'))