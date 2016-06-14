
import itertools

def checkio(N):
    table = [(0, 0)]
    for birds in itertools.accumulate(itertools.count(1)):
        prev_rec = table[-1]
        total_feeds = prev_rec[1] + birds
        current_rec = (birds, total_feeds)
        table.append(current_rec)

        if N <= total_feeds:
            repeat_eating = prev_rec[0] + prev_rec[1]
            if N < repeat_eating:
                return prev_rec[0]
            else:
                return current_rec[0] - (current_rec[1] - N)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(3) == 2, "2nd example"
    assert checkio(4) == 3, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"