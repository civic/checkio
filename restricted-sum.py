def checkio(data):
    if len(data) == 0:
        return 0
    else:
        return data[0] + checkio(data[1:])

if __name__ == "__main__":
    assert checkio([1, 2, 3]) == 6
    assert checkio([]) == 0
