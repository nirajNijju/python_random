

## https://codeshare.io/WdbDn8

## https://gist.githubusercontent.com/polyglothacker/2c5696dd8d25b8d7a626124c1bc8aeef/raw/1e8a4f87340dd62021700507918c91b3addd4ec4/stations.json
## https://gist.githubusercontent.com/polyglothacker/a9e58b06c834d56932eb50f4e20c85de/raw/d465dc3dc13cbdb93b449033687296335b03ada5/costs.json

## https://gist.github.com/polyglothacker/a9e58b06c834d56932eb50f4e20c85de
## https://gist.github.com/polyglothacker/2c5696dd8d25b8d7a626124c1bc8aeef


import sys
import json

class StationHelper:
    def __init__(self):
        with open('cost.json') as handle:
            self.cost_data = json.loads(handle.read())
        with open('station.json') as handle:
            self.stations_graph = json.loads(handle.read())

    # @classmethod
    # def find_all_paths(obj, graph, start, end, path=[]):
    #     path = path + [start]
    #     if start == end:
    #         return [path]
    #     if not  start in graph:
    #         return []
    #     paths = []
    #     for node in graph[start]:
    #         if node not in path:
    #             newpaths = obj.find_all_paths(graph, node, end, path)
    #             for newpath in newpaths:
    #                 paths.append(newpath)
    #     return paths

    def get_routes(obj, source, destination, route):
        if ord(source) > ord(destination):
            return None
        route = route + [source]
        if source == destination:
            # cost = obj.get_cost_for_route(route)
            # print("cost: {} | route : {}".format(cost, route))
            return  [route]
        new_route_list = []
        dest_stations = obj.stations_graph.get(source, None)
        if dest_stations is None:
            return  new_route_list
        for via in dest_stations:
            new_routes = obj.get_routes(via, destination, route)
            if new_routes:
                for new_route in new_routes:
                    new_route_list.append(new_route)
        return  new_route_list


    def get_cost_for_route(obj, route):
        if not route:
            return None
        source = route[0]
        total_cost = 0
        for i in range(1, len(route)):
            dest = route[i]
            key_cost = "{}->{}".format(source, dest)
            cost = obj.cost_data.get(key_cost)
            total_cost = total_cost + cost
            source = dest
        return total_cost

    def get_min_cost_between_stations(obj, source, destination):
        # route_list = obj.find_all_paths(obj.stations_graph, source, destination)
        route_list = obj.get_routes(source, destination, [])
        min_cost = sys.maxsize
        min_cost_route = None
        for route in route_list:
            cost = obj.get_cost_for_route(route)
            print("cost:{}   route: {}".format(cost , route))
            if min_cost > cost :
                min_cost = cost
                min_cost_route = route
        return min_cost, min_cost_route





