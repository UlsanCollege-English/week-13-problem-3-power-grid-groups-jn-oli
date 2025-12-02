def count_power_groups(stations, lines):
    # Build adjacency list
    graph = {station: [] for station in stations}

    for a, b in lines:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = 0

    def dfs(node):
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Count connected components
    for station in stations:
        if station not in visited:
            components += 1
            dfs(station)

    return components
