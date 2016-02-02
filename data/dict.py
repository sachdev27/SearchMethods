
def cities_graph():
    dict_graph = {}
    with open('data.txt', 'r') as f:
        for line in f:
            city_a, city_b, cost = line.strip().split(',')
            cost = int(cost)
            if city_a not in dict_graph:
                dict_graph[city_a] = {city_b: cost}
            else:
                dict_graph[city_a][city_b] = cost
            if city_b not in dict_graph:
                dict_graph[city_b] = {city_a: cost}
            else:
                dict_graph[city_b][city_a] = cost
    return dict_graph

cities_and_paths = cities_graph()
