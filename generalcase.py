# Two men have a 8-gallon jug full of wine and two empty jugs with a capacity of
# 5 and 3 gallons. They want to divide the wine into two equal parts. Suppose that when shifting
# wine from one jug to another, in order to know how much they have transferred, the men must
# always empty out the first jug or fill the second one (or both). Formulate this problem as a
# reachability problem in an appropriately defined graph.

# now the general case with n jugs


def pour(state, fromJug, toJug) -> None:
    """Pour wine from one jug to another, either fill the toJug or fully empty the fromJug. Inplace, so return none"""

    pourable = min(state[fromJug], capacities[toJug] - state[toJug])

    # Pour the wine
    state[fromJug] -= pourable
    state[toJug] += pourable

def dfs(curr, lim, target) -> bool:
    """DFS to find the target state in lim steps"""

    # Check base case for lim=0
    if lim == 0:
        return curr == target

    # Iterate over all possible pours
    for fromJug in range(len(curr)):
        for toJug in range(len(curr)):

            if fromJug != toJug:

                new_state = curr.copy()
                pour(new_state, fromJug, toJug)

                # recurse from new state onward
                if dfs(new_state, lim - 1, target):
                    return True

    return False

def isReachable(target, lim) -> bool:
    """Check if the target state is reachable in lim steps"""
    if lim < 0:
        return False

    return dfs(volumes, lim, target)


if __name__ == "__main__":
    inp = input("Enter Capacities: ")
    capacities = tuple(int(x) for x in inp.split(","))

    inp = input("Enter Starting volumes: ")
    inp = list(int(x) for x in inp.split(","))

    volumes = [0] * (len(capacities) - len(inp))
    volumes = inp + volumes

    inp = input("Enter Target: ")
    inp = list(int(x) for x in inp.split(","))
    target = [0] * (len(capacities) - len(inp))
    target = inp + target

    print(f"Capacities: {capacities}")
    print(f"Volumes: {volumes}")
    print(f"Target: {target}")

    print(isReachable(target, 100))




