# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    # build tree with array
    nodes = [[] for i in range(n)]
    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child
        else:
            nodes[parent].append(child)

    # traverse tree
    max_height = 0
    stack = [(root, 1)]
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        if nodes[node]:
            for i in nodes[node]:
                stack.append((i, height + 1))
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
