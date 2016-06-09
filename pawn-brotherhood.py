def safe_pawns(pawns):
    num_pawns = {(ord(x)-97, int(y)) for x, y in pawns}

    return sum(1 for _ in filter(lambda p: (p[0]-1, p[1]-1) in num_pawns or (p[0]+1, p[1]-1) in num_pawns, num_pawns))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1