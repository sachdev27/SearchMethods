import queue

from data.dict import cities_and_paths
from data.graph import Graph


def bfs_paths(start, goal):
    root = Graph(start, start, 0)
    q = queue.Queue()
    visited = []
    q.put(root)
    while not q.empty():
        obj = q.get()
        if obj.name == goal:
            print("\nThe path is", obj.path)
            print("\nThe cost is", obj.cost)
            return
        visited.append(obj)
        x = cities_and_paths[obj.name]
        for city, cost in x.items():
            if city in visited:
                continue
            else:
                node = Graph(name=city,
                             path=obj.path + ',' + city,
                             cost=obj.cost + cost)
                q.put(node)
