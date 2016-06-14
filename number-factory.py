def checkio(number):
    nums = []
    while number != 1:
        for n in range(9, 1, -1):
            if number % n == 0:
                nums.append(n)
                number /= n
                break
        else:
            return 0

    if nums:
        return int("".join(str(n) for n in reversed(nums)))
    else:
        return 0





if __name__ == '__main__':
    #print(search_max_digit([2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8) == 8
    assert checkio(16) == 28
    assert checkio(32) == 48
    assert checkio(27) == 39
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(560) == 2578, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(1536) == 3888, "5th example"
    assert checkio(9973) == 0, "6th example"
