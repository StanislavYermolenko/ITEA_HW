# number = ''
#
# while not isinstance(number, int):
#     try:
#         number = int(input('Please enter a number: '))
#     except ValueError:
#         print("Only numbers please")
#
# print(number + 10)

# a = {
#     'class 1a': ['Vasiliy', 'Nadejda'],
#     'class 2b': ['Andrey', 'Kostya'],
# }
#
# for key, value in a.items():
#     print(key, value)


# while True:
#     try:
#         number = int(input('Please enter a number: '))
#         break
#     except ValueError:
#         print("Only numbers please")
#
# even_numbers = []
# for i in range(number):
#     if i % 2 == 0:
#         continue
#     even_numbers.append(i)
#
# print(even_numbers)

# -------------------------------------- #
# Вывести среднюю оценку для каждого класса

# marks = {
#     '1a': [
#         ('Vasiliy', [9, 8, 12, 11, 5]),
#         ('Nadejda', [3, 10, 9, 10, 7])
#     ],
#     '2b': [
#         ('Andrey', [2, 3, 5, 9, 10]),
#         ('Kostya', [7, 8, 7, 8, 9])
#     ],
# }
#
# for class_, kids in marks.items():
#     mean_for_kids = []
#     for name, marks_ in kids:
#         mean_for_kids.append(sum(marks_) / len(marks_))
#
#     print(class_, sum(mean_for_kids) / len(mean_for_kids))


# -------------------------------------- #
# Если нам дана строка неопределенной длинны, определить
# является ли она палиндромом

# ропот и топор

# a = input("Input your string: ")
#
# # This is more memory efficient
# for index, letter in enumerate(a[:len(a) // 2], 1):
#     if letter != a[-index]:
#         print('this is not palindrome')
#         break
# else:
#     print('this is palindrome')
#
# # Same, but not memory efficient
# if a[:len(a) // 2] == a[len(a) // 2:][::-1]:
#     print('this is palindrome')
# else:
#     print('this is not palindrome')

#быстрый список от 0 до 10 list(range(10))






