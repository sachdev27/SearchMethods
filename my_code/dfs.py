from data.dict import cities_and_paths
from data.graph import Graph


def dfs_paths(start, goal):
    root = Graph(start, start, 0)
    stack = []
    visited = []
    stack.append(root)
    while len(stack) != 0:
        obj = stack.pop()
        if obj.name == goal:
            print("The path is", obj.path)
            print("The cost is", obj.cost)
            return
        visited.append(obj.name)
        x = cities_and_paths[obj.name]
        for city, cost in x.items():
            if city in visited:
                continue
            else:
                node = Graph(name=city,
                             path=obj.path + ',' + city,
                             cost=obj.cost + cost)
                stack.append(node)
