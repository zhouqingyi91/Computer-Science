def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = [[] for i in range(n)]
    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child
        else:
            nodes[parent].append(child)

    max_height = 0
    stack = [(root, 1)]
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        if nodes[node]:
            for i in nodes[node]:
                stack.append((i, height + 1))
    return max_height


print(compute_height(5, [-1, 0, 4, 0, 3]))
