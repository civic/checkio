import functools
import operator
import itertools
import collections

ACTIONS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "B": (0, 0)
}
MOVE = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

class Node:
    def __init__(self, pos, val):
        self.pos = pos
        """:type: tuple """
        self.val = val
        self.status = None
        """:type: str """
        self.r_cost = 0
        self.h_cost = 0
        self.score = 0
        self.parent = None
        self.route = ""
        """:type: Node """

    def open(self, goal, parent, move, cost):
        pos = self.pos
        self.parent = parent

        r_cost = self.parent.r_cost + cost if self.parent is not None else 0
        h_cost = (goal[0] - pos[0]) + (goal[1] - pos[1])
        score = r_cost + h_cost

        if (self.status is not None) and (self.score < score):
            return

        self.r_cost = r_cost
        self.h_cost = h_cost
        self.score = score
        self.status = "O"

        if move is not None:
            self.route = parent.route + move

    def __eq__(self, other):
        return other.pos == self.pos

    def __ne__(self, other):
        return other.pos != self.pos

    def __hash__(self):
        return self.pos.__hash__()
    def __repr__(self):
        return "({pos[0]},{pos[1]}){v}:{status},{r_cost},{h_cost},{score}".format(
            pos=self.pos,
            v = self.val,
            status=self.status if self.status is not None else "-",
            r_cost=self.r_cost,
            h_cost=self.h_cost,
            score=self.score
        )


def search_a_star(start, goal, nodes, cost):
    max_row = len(nodes)
    max_col = len(nodes[0])
    start_node = nodes[start[0]][start[1]]
    start_node.open(goal, None, None, 0)
    open_list = set()
    open_list.add(start_node)

    while len(open_list) > 0:
        min_score_node = min(open_list, key=lambda n: n.score)
        for node in [n for n in open_list if n.score == min_score_node.score]:
            pos = node.pos

            for move in MOVE.items():
                move_direction = move[0]
                m = move[1]
                new_y = pos[0]+m[0]
                new_x = pos[1]+m[1]
                if new_y < 0 or max_row <= new_y:
                    continue
                elif new_x < 0 or max_col <= new_x:
                    continue
                next_node = nodes[new_y][new_x]
                if next_node.val == 'W':
                    continue
                if next_node.status in ("C", ):
                    continue

                next_node.open(goal, node, move_direction, cost)
                if next_node.pos == goal:
                    return next_node

                open_list.add(next_node)

            open_list.remove(node)
            node.status = "C"

def box_route_search(start, goal, nodes, boxes, limit_score):
    relay_points = collections.deque()
    for bpos in boxes:
        relay_points.append(bpos)
    relay_points.append(goal)


    route = ""
    score = 0
    from_pos = start
    for have in itertools.cycle((True, False)):
        to_pos = relay_points.popleft()

        clone_nodes = [[Node(n.pos, n.val) for n in row] for row in nodes]
        found = search_a_star(from_pos, to_pos, clone_nodes, 2 if have else 1)
        if found is None:
            return 999999, None
        route += found.route
        score += found.score

        if score > limit_score:
            return 999999, None

        if found.val == "B":
            route += "B"
            score += 1

        if len(relay_points) == 0:
            break
        from_pos = to_pos
    return score, route



def checkio(field_map):
    nodes = [[Node((y, x), v) for x, v in enumerate(row)] for y, row in enumerate(field_map)]

    start, goal = None, None
    boxes = []
    for n in itertools.chain(*nodes):
        if n.val == "S":
            start = n.pos
        elif n.val == "E":
            goal = n.pos
        elif n.val == "B":
            boxes.append(n.pos)

    min_route = None
    min_score = 999999
    cnt = 0
    for n in [0, 2]:#range(0, len(boxes)+1, 2):
        for box_routes in itertools.permutations(boxes, n):
            if cnt > 10000:
                raise ValueError("overflow cnt")
            cnt += 1

            score, route = box_route_search(start, goal, nodes, box_routes, min_score)
            if route is not None:
                print("{0}\t{1}\t".format(score, route, box_routes))

            if score < min_score:
                min_score = score
                min_route = route

    return min_route


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    # assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    # assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
    # assert check_solution(checkio, 18, [
    #     "SBW...",
    #     ".WWB..",
    #     "..WW..",
    #     "......",
    #     "...WW.",
    #     "..BWBE",
    # ]), "3nd example"
    assert check_solution(checkio, 13, [
        "SBBBBB",
        "BBBBBB",
        "BBBBBB",
        "BBBBBB",
        "BBBBBE"])
