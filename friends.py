import itertools

class Friends:
    def __init__(self, connections):
        self.connections = set((a, b) for a, b in connections)

    def add(self, connection):
        connection = tuple(connection)
        if connection in self.connections:
            return False
        else:
            self.connections.add(connection)
            return True

    def remove(self, connection):
        connection = tuple(connection)
        if connection not in self.connections:
            return False
        else:
            self.connections.remove(connection)
            return True

    def names(self):
        return set(itertools.chain(*self.connections))

    def connected(self, name):
        friends = set()
        for con in self.connections:
            s = set(con)
            if name in s:
                friends.add(list(s - set((name,)))[0])

        return friends



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    assert f.connected("nikola") == {"sophia"}