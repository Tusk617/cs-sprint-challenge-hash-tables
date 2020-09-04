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
    route = [0]
    # for ticket in tickets:
    #     flightPlan[ticket.destination] = ticket.source
    #     print(flightPlan)
    # for flight in flightPlan:
    #     print(flight)
    #     route.append(flight)
    # # print(flightPlan)
    # print(route)
    for i in tickets:
        flightPlan[i.source] = i.destination
         
    # print(flightPlan)

    return route
