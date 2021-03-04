#increase
# while True:
#
#     a = int(input('input number: '))
#     for i in range(a):
#         print('*' * a)
#         a -= 1
#         if a == 0:
#             break

#decrease
# while True:
#
#     a = int(input('input number: '))
#     b = 0
#     while b <= a:
#         print('*' * b)
#         b += 1

#add_task
while True:
    a = int(input('input number: '))
    for i in range(a):
        b = a - i
        print(' ' * b + '*' * i + '*' * i)

