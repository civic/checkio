import functools
def checkio(number):
    return functools.reduce(lambda a,b: a*b, (int(c) for c in str(number) if c != "0"))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
