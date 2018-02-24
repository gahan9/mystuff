"""https://code.google.com/codejam/contest/4374486/dashboard#s=p2
Problem C. Sort a scrambled itinerary

Once upon a day, Mary bought a one-way ticket from somewhere to somewhere with some flight transfers.

For example: SFO->DFW DFW->JFK JFK->MIA MIA->ORD.

Obviously, transfer flights at a city twice or more doesn't make any sense. So Mary will not do that.

Unfortunately, after she received the tickets, she messed up the tickets and she forgot the order of the ticket.

Help Mary rearrange the tickets to make the tickets in correct order.
"""


def endpoint_finder(flight_tickets):
    origin, endpoint = '', ''
    for k, v in flight_tickets.items():
        if k not in flight_tickets.values():
            origin = k
        if v not in flight_tickets.keys():
            endpoint = v
    return origin, endpoint


def route_maker(flight_tickets, origin, end, st=""):
    st += " " + origin
    dest_of_curr_origin = flight_tickets[origin]
    if dest_of_curr_origin == end:
        return st + "-" + end
    else:
        st += "-" + dest_of_curr_origin
        return route_maker(flight_tickets, dest_of_curr_origin, end, st)


if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        flights = {}
        for j in range(1, n + 1):
            source = input()
            destination = input()
            flights[source] = destination
        s, d = endpoint_finder(flights)
        travel_path = route_maker(flights, s, d)
        print("Case #{}: {}".format(i, travel_path.strip()))
