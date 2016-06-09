import functools

def get_one(*args, left=True, **kwargs):
    key = kwargs.get("key", lambda x: x)
    seq = args if len(args) > 1 else args[0]

    def comp(a, b):
        if key(a) >= key(b):
            return a if left else b
        else:
            return b if left else a

    return functools.reduce(comp, seq)

def min(*args, **kwargs):
    return get_one(*args, left=False, **kwargs)


def max(*args, **kwargs):
    return get_one(*args, left=True, **kwargs)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
