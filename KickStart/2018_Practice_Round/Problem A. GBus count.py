"""https://code.google.com/codejam/contest/4374486/dashboard
Problem A. GBus count

There exists a straight line along which cities are built.

Each city is given a number starting from 1. So if there are 10 cities, 
city 1 has a number 1, city 2 has a number 2,... city 10 has a number 10.

Different buses (named GBus) operate within different cities, covering all the cities along the way. 
The cities covered by a GBus are represented as 'first_city_number last_city_number' 
So, if a GBus covers cities 1 to 10 inclusive, the cities covered by it are represented as '1 10'

We are given the cities covered by all the GBuses. 
We need to find out how many GBuses go through a particular city.
"""


class GBus(object):
    @staticmethod
    def get_gbus_relation(city_list):
        return {city_list[x]: city_list[x+1] for x in range(0, len(city_list)-1, 2)}

    @staticmethod
    def gbus_lookup(relations, lookup_city):
        result = 0
        for key, value in relations.items():
            if key <= lookup_city <= value:
                result += 1
        return str(result)

if __name__ == "__main__":
    bus_obj = GBus()
    # input case 1
    t = int(input())  # read a line with a single integer total test case (T)
    for i in range(1, t + 1):
        number_of_buses = int(input())  # read number of buses from input
        cities = [int(s) for s in input().split(" ")]  # read a list of integers, total cities
        gbus_relation = bus_obj.get_gbus_relation(city_list=cities)
        # print("Case #{}: {} {}".format(i, n + m, n * m))
        # input case 2
        total_cities_for_lookup = int(input())
        gbus_through_city = []
        for cities in range(1, total_cities_for_lookup + 1):
            city = int(input())
            gbus_through_city.append(bus_obj.gbus_lookup(gbus_relation, city))
        print("Case #{}: {}".format(i, " ".join(gbus_through_city)))
