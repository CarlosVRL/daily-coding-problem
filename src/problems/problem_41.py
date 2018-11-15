"""
Module problem_41

Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's
itinerary.

If no such itinerary exists, return null.

If there are multiple possible itineraries, return the lexicographically
smallest one. All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A', you should return the list
['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C']
is also a valid itinerary. However, the first one is lexicographically smaller.
"""


def compute_itinerary(flights, start):

    res = []

    origin_to_destination_map = generate_origin_to_destination_map(flights)

    if len(origin_to_destination_map) == 0:
        return None

    while True:

        if start in origin_to_destination_map:
            res.append(start)
            next_origin = origin_to_destination_map[start]
            origin_to_destination_map.pop(start)
            start = next_origin
            continue

        if len(origin_to_destination_map) == 0:
            res.append(start)
            return res
        else:
            return None


def generate_origin_to_destination_map(flights):

    origin_to_destination_map = {}

    origin_index = 0
    destination_index = 1

    for flight in flights:
        origin_to_destination_map[flight[origin_index]] = flight[destination_index]

    return origin_to_destination_map
