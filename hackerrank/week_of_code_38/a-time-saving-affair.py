#!/bin/python3
"""
https://www.hackerrank.com/contests/w38/challenges/a-time-saving-affair
=======================================================================
Janet is in an Uber on her way to an interview. The driver promises to take her to the venue as soon as possible. The driver is aware that:

    There are junctions in the city of Mumbai, numbered from to .
    Janet's interview location is at junction . They are initially at junction .
    There are bidirectional roads connecting some pairs of junctions, each one requiring some amount of time to pass through it.

At every junction, there are traffic lights denoting whether they are allowed to go further or to wait. Traffic lights have two colors, and . The driver can commute through junctions based on these conditions:

    At any junction, if the traffic signal's light is green, then they can go immediately, otherwise, they have to wait until traffic signal becomes green.
    Traffic signal changes its color every seconds of time at all junctions simultaneously.

Initially, at the second, all traffic lights have changed to green color at all the junctions. If the cab driver reaches a junction at a second when the traffic light changes its color, then he sees the traffic light after the change.

Can you help the driver determine the least amount of time needed to reach the interview location?

Complete the function leastTimeToInterview which takes in three integers , and and returns the least amount of time needed to reach the interview location, in seconds. You need to take the information about the roads from the standard input. They will be specified in lines, as described in the input format section below.

Input Format

The first line contains an integer , the number of junctions.

The second line contains an integer denoting the time taken by a signal to change its color.

The third line contains an integer denoting the number of roads.

The next lines describe the roads. Each consist of three space-separated integers , and where and denotes a road between two junctions and denotes time required to travel through it.

Constraints

    There can be self-loops, i.e., roads connecting a junction to itself.
    There is at least one path from junction to junction .

Output Format

Print a single integer denoting the shortest amount of time required to reach junction .

Sample Input 0

7
4
7
1 2 3
2 3 1
1 4 4
4 6 7
7 5 2
3 5 1
4 5 5

Sample Output 0

11

Explanation 0

    Junction number : The cab driver can visit any of the adjacent junctions. He chooses to visit junction . Since the traffic signal is at the second, He can visit junction which takes seconds.

    Junction number : The traffic signal is still since traffic signals change color every seconds. The cab driver now chooses to visit junction which takes second, and we are now at the second.

    Junction number : seconds have passed, and the traffic signal has already become . They have to wait for more seconds until the signal again becomes .

    Junction number : The cab takes the route to junction which takes second. So far, seconds have passed.

    Junction number : The traffic signal is still and the cab can go to junction . It takes seconds to reach junction .

In total, it takes seconds to go from junction to junction . It can be shown that this is the minimum amount of time possible.
https://s3.amazonaws.com/hr-assets/0/1529397919-1f313653ec-min3.png
"""

import os


def find_all_paths(graph, start, end, travel_duration=0, path=[]):
    path = path + [(start, travel_duration)]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for route in graph[start]:
        node, duration = route
        if node not in map(lambda x: x[0], path):
            new_paths = find_all_paths(graph, node, end, duration, path=path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


# Complete the leastTimeToInterview function below.
def leastTimeToInterview(n, k, m):
    start_node = 1
    final_destination = n
    road_map = {}
    road_map_jn = {}
    for _ in range(m):
        junction1, junction2, travel_time = map(int, input().strip().split())
        # road_map[src] = road_map.get(src, set())
        # road_map[src].add((dest, travel_time))  # append destination with travel time in dict
        # road_map[dest] = road_map.get(dest, set())
        # road_map[dest].add((src, travel_time))
        # road_map_jn[junction1] = road_map_jn.get(junction1, [])
        # road_map_jn[junction2] = road_map_jn.get(junction2, [])
        # road_map_jn[junction2] = road_map_jn[junction2] + [junction1] if junction1 not in road_map_jn[junction2] else road_map_jn[junction2]  # append destination with travel time in dict
        # road_map_jn[junction1] = road_map_jn[junction1] + [junction2] if junction2 not in road_map_jn[junction1] else road_map_jn[junction1]  # append destination with travel time in dict
        road_map[junction1] = road_map.get(junction1, [])
        road_map[junction2] = road_map.get(junction2, [])
        road_map[junction2] = road_map[junction2] + [(junction1, travel_time)] if (junction1, travel_time) not in road_map[junction2] else road_map[junction2]  # append destination with travel time in dict
        road_map[junction1] = road_map[junction1] + [(junction2, travel_time)] if (junction2, travel_time) not in road_map[junction1] else road_map[junction1]  # append destination with travel time in dict
        # print(junction1, junction2, road_map_jn)
    # print(road_map)
    routes = find_all_paths(road_map, start_node, final_destination, travel_duration=0)
    # print(routes)
    min_time = 10**100
    flag = True
    for route in routes:
        meter_time = 0
        for junction in route:
            if flag:
                meter_time += junction[1]
            else:
                meter_time += junction[1] + 4
            flag = True if meter_time % 8 in range(4) else False
        if meter_time < min_time:
            min_time = meter_time
    return min_time


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    k = int(input())
    m = int(input())
    result = leastTimeToInterview(n, k, m)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
