from itertools import groupby


def transaction(file):
    """
    Transformation of string.\n
    :param file: take address of file with string in it
    :type file: str
    :return: str
    """

    hw_file = open(file, "r+")

    work = hw_file.read()

    groups = groupby(work, str.isdigit)

    expanded = []

    for is_numeric, characters in groups:

        if is_numeric:
            expanded.append(expanded[-1] * (int(''.join(characters)) - 1))
        else:
            expanded.extend(characters)
    res = ''.join(expanded)

    print('WAS:', work)
    print('CHANGE TO:', res)

    hw_file.close()

    new_file = open('new_file_w.txt', "w")
    new_file.write(res)
    new_file.close()
    return "new_file_w.txt"


if __name__ == 'main':
    result = transaction('text_for_hw.txt')
    hw_file = open(result)
    work = hw_file.read()
    # print(work) if delete print from function, make this line active

