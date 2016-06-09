class Node:
    def __init__(self, name):
        self.name = name
        self.links = {}

    def __str__(self):
        return "<" + self.name + ">"

def check_connection(network, first, second):
    node_map = {}
    """ :type: dict[str, Node] """
    for elm in network:
        node_strs = elm.split("-")

        left = node_map.get(node_strs[0]) or Node(node_strs[0])
        right = node_map.get(node_strs[1]) or Node(node_strs[1])

        left.links[right.name] = right
        right.links[left.name] = left
        node_map[left.name] = left
        node_map[right.name] = right

    def search(history, target, end):
        for link_node in target.links.values():
            if link_node.name == end.name:
                return True
            elif link_node.name not in history:
                history.add(target.name)
                if search(history, link_node, end):
                    return True

        return False

    start = node_map[first]
    end = node_map[second]
    return search(set(), start, end)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
