import heapq
import pandas as pd
import networkx as nx
from models.data_models import Models


def single_source_dijkstra_path(G, source, weight="weight"):
    lengths = {}
    paths = {}

    queue = [(0, source)]
    lengths[source] = 0

    while queue:
        (dist, node) = heapq.heappop(queue)

        for neighbor in G[node]:
            new_dist = dist + G[node][neighbor].get(weight, 1)
            if neighbor not in lengths or new_dist < lengths[neighbor]:
                lengths[neighbor] = new_dist
                paths[neighbor] = paths.get(node, []) + [neighbor]
                heapq.heappush(queue, (new_dist, neighbor))

    return paths


def calculate_total_time(path, time_map):
    total_time = 0
    for i in range(len(path) - 1):
        station1 = path[i]
        station2 = path[i + 1]

        if (station1, station2) in time_map:
            total_time += time_map[(station1, station2)]
        elif (station2, station1) in time_map:
            total_time += time_map[(station2, station1)]

    return total_time


def create_graph():
    graph = nx.Graph()

    subway_stations = Models.subway_stations
    interchange_connections = Models.interchange_connections

    for line, stations in subway_stations.items():
        for station in stations:
            graph.add_node(f"{station} ({line})")

    for line, stations in subway_stations.items():
        for i in range(len(stations) - 1):
            graph.add_edge(f"{stations[i]} ({line})", f"{stations[i+1]} ({line})")

    graph.add_edges_from(interchange_connections)

    return graph


def add_connecitons(graph):
    line_colors = {
        "U1": "#51832b",
        "U2": "#c4002d",
        "U3": "#ed6721",
        "U4": "#00ab86",
        "U5": "#be7b00",
        "U6": "#0264af",
        "U7": "purple",
        "U8": "brown",
    }

    interchange_connections = Models.interchange_connections
    unique_stations = set()

    for connection in interchange_connections:
        unique_stations.add(connection[0])
        unique_stations.add(connection[1])

    transit_station_size = 150
    line_station_size = 100

    node_sizes = []
    node_colors = []

    for node in graph.nodes():
        if any(station in node for station in unique_stations):
            node_sizes.append(transit_station_size)
        else:
            node_sizes.append(line_station_size)

        for line, color in line_colors.items():
            if f"({line})" in node:
                node_colors.append(color)
                break

    return graph, node_sizes, node_colors


def print_shortest_path_table():
    graph, node_sizes, node_colors = add_connecitons(create_graph())
    # Set the source station as "Hauptbahnhof (U1)"
    source_station = "Hauptbahnhof (U1)"

    shortest_paths = single_source_dijkstra_path(graph, source_station)

    data = {
        "Source": [],
        "Target": [],
        "Shortest Path": [],
        "Path Length": [],
        "Travel Time": [],
    }
    for target, path in shortest_paths.items():
        path_length = nx.dijkstra_path_length(graph, source_station, target)

        data["Source"].append(source_station)
        data["Target"].append(target)
        data["Shortest Path"].append(path)
        data["Path Length"].append(path_length)
        data["Travel Time"].append(calculate_total_time(path, Models.edge_weights))

    df = pd.DataFrame(data)

    print("\nShortest Paths Table:")
    print(df)
