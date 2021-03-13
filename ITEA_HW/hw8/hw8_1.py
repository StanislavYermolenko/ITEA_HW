def acr(phrase):
    """
    Acronym Generator.\n
    :param phrase: take phrase from user
    :type phrase: str
    :return: str
    """
    a = ''
    for word in phrase.replace('of', '').split():
        a = a + word[0].upper()

    print(f'Acronym of "{phrase}" is {a}')


if __name__ == '__main__':
    text = input('Enter a phrase: ')
    acr(text)

