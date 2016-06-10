import re
import itertools
def find_word(message):

    def calc(w1, w2):
        likeness = 0
        likeness += 10 if w1[0] == w2[0] else 0
        likeness += 10 if w1[-1] == w2[-1] else 0
        likeness += min(len(w1), len(w2)) / max(len(w1), len(w2)) * 30

        u1 = set(w1)
        u2 = set(w2)
        likeness += len(u1.intersection(u2)) / len(u1.union(u2)) * 50

        return likeness

    list_of_index_and_word = [(n, re.sub(r'[^A-z]', '', w.lower())) for n, w in enumerate(message.split(" "))]

    def sum_likeness(p1):
        n1, w1 = p1
        return sum(calc(w1, w2) for n2, w2 in list_of_index_and_word if n1 != n2), n1

    return max(list_of_index_and_word, key=sum_likeness)[1]




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Friend Fred and friend Ted.") == "friend"
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy. According to a researcher at Cambridge University.") == "according"