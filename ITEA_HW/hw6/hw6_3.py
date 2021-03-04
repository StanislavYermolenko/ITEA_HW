
a = int(input('input number: '))
b = list(range(2, a + 1))
for x in b:
    if x != 0:
        for y in range(2 * x, a + 1, x):
            b[y - 2] = 0
print(*list(filter(lambda x: x != 0, b)))

