dict_graph = {}


# Read the data.txt file
with open('/media/divine/Sandesh/study/Sem6/AI/TA-IDS/SearchMethods/distance5.txt', 'r') as f:
    for l in f:
        # print(l)
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = float(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = float(p_cost)


# Iterative Deepening Search Method
def IterativeDeepening(graph, src, dst):
    level = 0
    count = 0
    stack = [(src, [src], 0)]
    visited = {src}
    while True:
        level += 1
        while stack:
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in graph[node].keys():
                    if temp == dst:
                        return path + [temp], cost + graph[node][temp]
                    else:
                        if temp not in visited:
                            visited.add(temp)
                            count += 1
                            stack.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                q = stack
                visited_bfs = {src}
                while q:
                    (node, path, cost) = q.pop(0)
                    for temp in graph[node].keys():
                        if temp == dst:
                            return path + [temp], cost + graph[node][temp]
                        else:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                break


n = 1
# print(dict_graph)
print("------------------------------------------------")

src = input("Enter the source:")
dst = input("Enter the Destination: ")
while src not in dict_graph or dst not in dict_graph:
    print("No such city name")
    src = input("Enter the correct source (case_sensitive):\n")
    dst = input("Enter the correct destination(case_sensitive):\n")
print("for ID")
print (IterativeDeepening(dict_graph, src, dst))


