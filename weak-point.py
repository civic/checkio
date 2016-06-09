def weak_point(matrix):
    row_sums = [sum(row) for row in matrix]
    min_row_sum = min(row_sums)

    col_sums = [sum([row[c] for row in matrix]) for c in range(len(matrix[0]))]
    min_col_sum = min(col_sums)

    return row_sums.index(min_row_sum), col_sums.index(min_col_sum)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                             [2, 9, 4, 1, 7],
                             [3, 8, 6, 2, 4],
                             [2, 5, 2, 9, 1],
                             [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
