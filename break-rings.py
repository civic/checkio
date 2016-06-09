import itertools

def remain_rings(connections):
    return set(itertools.chain(*connections))

def remain_links(ring, connections):
    return [pair for pair in connections if ring not in pair]

def check_breaks(break_rings, connections):
    remain = connections
    for r in break_rings:
        remain = remain_links(r, remain)

    return len(remain)


def break_rings(connections):
    rings = remain_rings(connections)

    for n in range(1, len(rings)):
        for ptn in itertools.combinations(rings, n):
            if check_breaks(ptn, connections) == 0:
                return n


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)) == 5
    assert break_rings(({1, 9}, {1, 2}, {8, 5}, {4, 6}, {5, 6}, {8, 1}, {3, 4}, {2, 6}, {9, 6}, {8, 4}, {8, 3}, {5, 7}, {9, 7}, {2, 3}, {1, 7},)) == 5
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 2}, {1, 6}, {6, 7}, {7, 8}, {8, 9}, {9, 6}, {1, 10}, {10, 11}, {11, 12}, {12, 13}, {13, 10}, {1, 14}, {14, 15}, {15, 16}, {16, 17}, {17, 14},)) == 8
