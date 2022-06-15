# for testing ..


from min_cost import *  

station_helper = StationHelper()

station_helper.stations_graph


station_helper.get_min_cost_between_stations('A', 'Z') ## Valid path

station_helper.get_min_cost_between_stations('A', 'X') ## Valid path

station_helper.get_min_cost_between_stations('A', 'B') ## NOT a Valid path

station_helper.get_min_cost_between_stations('A', 'Y') ## NOT a Valid path
