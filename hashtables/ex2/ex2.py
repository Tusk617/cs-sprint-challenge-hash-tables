#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # for i in tickets:
    #     print(i.source)
    flightPlan = {}
    route = []
    current = "NONE"
    next = "NONE"
    # for ticket in tickets:
    #     flightPlan[ticket.destination] = ticket.source
    #     print(flightPlan)
    # for flight in flightPlan:
    #     print(flight)
    #     route.append(flight)
    # # print(flightPlan)
    # print(route)
    for ticket in tickets:
        flightPlan[ticket.source] = ticket.destination
        # print(flightPlan)

    while len(route) <= length:
        for flight in flightPlan:
            if flightPlan[next] == "NONE":
                route.append(flightPlan[next])
                print(route)
                return route
            if flight == next:
                route.append(flightPlan[next])
                next = flightPlan[flight]
                # route.append(flightPlan[next])
                # print(route)
    
    # return route
