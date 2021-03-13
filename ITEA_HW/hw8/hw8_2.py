def alldiv(num):

    """
    Takes a number ans displays all of its divisors.\n
    :param num: number for action
    :type num: int
    :return: List[int]
    """

    divisors = [x for x in range(1, num + 1)
                if num % x == 0]
    return divisors


print(alldiv(36))


def alldivisors(num):

    """
    Find all divisors of put number.\n
    :param num: int
    :return: int

    """

    for x in range(1, num + 1):
        if num % x == 0:
            print(x, end=' ')


alldivisors(36)

