import datetime
def most_frequent_days(year):
    first_day = datetime.date(year, 1, 1)
    last_day = datetime.date(year, 12, 31)

    # counter
    counter = [0] * 7   #[monday_count, tuesday_count, ...]

    # count first week
    for dow in range(first_day.weekday(), 7):
        counter[dow] += 1

    # count last week
    for dow in range(0, last_day.weekday() + 1):
        counter[dow] += 1

    max_count = max(counter)
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    ret = []
    for dow, count in enumerate(counter):
        if count == max_count:
            ret.append(names[dow])

    return ret

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
