import collections

def checkio(marbles, org_step):
    print(marbles, org_step)

    total = len(marbles)
    q = collections.deque()
    q.append((1, 1.0, marbles))

    while any((p[0] < org_step for p in q)):
        step, probability, now_marbles = q.popleft()

        white = now_marbles.count("w")
        if white != 0:
            white_pattern = step+1, probability * white / total, now_marbles.replace("w", "b", 1)
            q.append(white_pattern)


        black = now_marbles.count("b")
        if black != 0:
            black_pattern = step+1, probability * black / total, now_marbles.replace("b", "w", 1)
            q.append(black_pattern)

    final_probability = 0
    for ptn in q:
        step, probability, now_marbles = ptn
        white = now_marbles.count("w")
        final_probability +=  white / total * probability

    return round(final_probability, 2)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('wbb', 3) == 0.48, "1st example"
    #assert checkio('bbw', 3) == 0.48, "1st example"
    #assert checkio('wwb', 3) == 0.52, "2nd example"
    #assert checkio('www', 3) == 0.56, "3rd example"
    #assert checkio('bbbb', 1) == 0, "4th example"
    #assert checkio('wwbb', 4) == 0.5, "5th example"
    #assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    #assert checkio('bwbwbwbbbwwbwbwbbwb', 20) == 0.49, "6th example"
