from itertools import combinations
def is_palindromic(text):
    return text == text[::-1]

def longest_palindromic(text):
    longest = ""
    for s, e in combinations(range(len(text) + 1), 2):
        substr = text[s:e]
        if is_palindromic(substr) and len(longest) < len(substr):
            longest = substr

    return longest

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
