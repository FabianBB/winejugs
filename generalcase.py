# Two men have a 8-gallon jug full of wine and two empty jugs with a capacity of
# 5 and 3 gallons. They want to divide the wine into two equal parts. Suppose that when shifting
# wine from one jug to another, in order to know how much they have transferred, the men must
# always empty out the first jug or fill the second one (or both). Formulate this problem as a
# reachability problem in an appropriately defined graph.

# now the general case with n jugs

import sys

def isValidState() -> bool:
    """Basic check to see if any obvious constraints are violated, i.e. capacity and non-negativity"""
    for i in range(len(volumes)):
        if volumes[i] > capacities[i] or volumes[i] < 0:
            return False

    return True

def pour(state, fromJug, toJug) -> None:
    """Pour wine from one jug to another, either fill the toJug or fully empty the fromJug. Inplace, so return none"""

    # determine how much wine can be poured
    pourable = min(state[fromJug], capacities[toJug] - state[toJug])

    # Pour the wine
    state[fromJug] -= pourable
    state[toJug] += pourable


def dfs(curr, lim, target, capacities) -> bool:
    """DFS to find the target state in lim steps"""

    # Check base case for lim=0
    if lim == 0:
        return curr == target
    # base case
    if curr == target:
        return True

    # Iterate over all possible pours
    for fromJug in range(len(curr)):
        for toJug in range(len(curr)):

            # if the target jug is full or the fromJug is empty, skip the iteration since nothing happens
            # saves some time
            if capacities[toJug] == curr[toJug] or curr[fromJug] == 0:
                continue

            # cant pour into the same jug
            if fromJug != toJug:

                new_state = curr.copy()
                pour(new_state, fromJug, toJug)

                # recurse from new state onward
                if dfs(new_state, lim - 1, target, capacities):
                    return True

    return False


def isReachable(target, lim, capacities) -> bool:
    """Check if the target state is reachable in lim steps"""
    if lim < 0:
        return False

    return dfs(volumes, lim, target, capacities)


# main method (imagine public static void main(String[] args) in Java)
if __name__ == "__main__":
    inp = input("Enter Capacities: ")
    capacities = tuple(int(x) for x in inp.split(","))

    inp = input("Enter Starting volumes: ")
    inp = list(int(x) for x in inp.split(","))

    # lazy way to pad input with 0s
    volumes = [0] * (len(capacities) - len(inp))
    volumes = inp + volumes

    inp = input("Enter Target: ")
    inp = list(int(x) for x in inp.split(","))

    # same thing
    target = [0] * (len(capacities) - len(inp))
    target = inp + target

    print(f"Capacities: {capacities}")
    print(f"Volumes: {volumes}")
    print(f"Target: {target}")

    # if the input state is not valid then exit
    if not isValidState():
        print("Invalid State")
        sys.exit(1)

    print("Target state is reachable:", isReachable(target, 100, capacities))
