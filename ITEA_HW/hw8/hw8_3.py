from itertools import groupby

hw_file = open('text_for_hw8_3.txt', "r+")

work = hw_file.read()

groups = groupby(work, str.isdigit)

expanded = []

for is_numeric, characters in groups:

    if is_numeric:
        expanded.append(expanded[-1] * (int(''.join(characters)) - 1))
    else:
        expanded.extend(characters)
res = ''.join(expanded)
print(res)
print(work)

hw_file.close()

new_file = open('output.txt', "w")
new_file.write(res)
new_file.close()

