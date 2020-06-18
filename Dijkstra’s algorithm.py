def djAlgo(nodes,distances,start):
    unvisited = {node:None for node in nodes}
    visited = {}
    current = start
    current_distance = 0
    unvisited[current] = current_distance
    path =[]
    while True:
        for neighbor, distance in distances[current].items():

            if neighbor not in unvisited:
                continue
            new_distance= current_distance + distance
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance

        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1]) [0]
    least_distance = visited['San Francisco']
    least_city = 'San Francisco'
    if visited['Seattle'] < least_distance:
        least_city = 'Seattle'
        least_distance = visited['Seattle']
    if visited['Los Angeles']  < least_distance:
        least_city = 'Los Angeles'
        least_distance = visited['Los Angeles']
    print("closest city is " +least_city + " and distance is " +str(least_distance))
    return least_city
#recursive method to find shortest path
def dijkstra_shortest(graph, src, dest, visited=[], distances={}, predecessors={}):
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
       # code to end the loop
    if src == dest:
        # building shortest path to display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        path.reverse()
        print('shortest path: ' + str(path)+ " cost=" + str(distances[dest]))
    else:
        # initializing the costs
        if not visited:
            distances[src] = 0
        # visiting the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # marking it as visited once done
        visited.append(src)
        # recurse to find select the non visited node with lowest distance 'x'
        # run Dijskstra with source as 'x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra_shortest(graph, x, dest, visited, distances, predecessors)

#function to convert to cost
def convertToCost(distance):
    cost = 0
    if distance >= 2000:
        cost =  1000*0.005 + 1000*0.004 + 0.003*(distance-2000)
    elif distance >1000:
        cost = 1000*0.005 + (distance-1000)*0.004
    else:
        cost = distance*0.005
    return cost
#cost based algorithm
def djAlgoCost(nodes,distances,start):
    unvisited = {node:None for node in nodes}
    visited = {}
    current = start
    current_cost = 0
    unvisited[current] = current_cost

    while True:
        for neighbor, distance in distances[current].items():

            if neighbor not in unvisited:
                continue
            new_cost= current_cost + convertToCost(distance)
            if unvisited[neighbor] is None or unvisited[neighbor]> new_cost:

                unvisited[neighbor] = new_cost

        visited[current] = current_cost
        del unvisited[current]
        #print("enteres del okay")
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_cost = sorted(candidates, key=lambda x: x[1]) [0]
    least_cost = visited['San Francisco']
    least_city = 'San Francisco'
    if visited['Seattle'] < least_cost:
        least_city = 'Seattle'
        least_cost = visited['Seattle']
    if visited['Los Angeles']  < least_cost:
        least_city = 'Los Angeles'
        least_cost = visited['Los Angeles']
    print("closest city is " +least_city + " and distance is " +str(least_cost))

#applying copy logic on dictionary
def minus_key(start, visited):
        shallow_copy = dict(visited)
        del shallow_copy[start]
        return shallow_copy

#code to just find out the nearest neighbour for a start point
def dijkstra(nodes,distances,start):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = start
    current_distance = 0
    unvisited[current] = current_distance
    least_distance =0
    while True:
        # print("next while start")
        # print("unvisited to start : ")
        # print(unvisited)
        for neighbor, distance in distances[current].items():
            # print("enteres for okay")
            if neighbor not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                # print("enteres if okay")
                unvisited[neighbor] = new_distance
            # print("unvisited to start : ")
            # print(unvisited)
        visited[current] = current_distance
        # print("visited to start : ")
        #print(visited)
        # print(current)
        del unvisited[current]
        # print("enteres del okay")
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

    new = minus_key(start,visited)
    n = len(new)
    least_distance = new.values()[0]
    for i in range(1,n):
        distance = new.values()[i]
        if least_distance >= distance:
            least_distance = distance
        i = i+1

    print("Nearest neighbour from start location is at a distance of" )
    print(str(least_distance))


nodes=('Boston', 'New York' ,'Washington DC' ,'Miami' ,'Chicago' ,'Minneapolis', 'Dallas', 'Denver', 'Seattle', 'San Francisco', 'Las Vegas', 'Los Angeles')
distances={

'New York' : {'Boston' : 338, 'Washington DC' : 383, 'Miami' : 2145},
'Boston' : { 'New York' : 338, 'Washington DC' : 725, 'Chicago' : 1613},
'Washington DC' : {'New York' : 383, 'Boston' : 725, 'Chicago' : 1145, 'Miami' : 1709, 'Dallas' : 2113},
'Miami' : {'Washington DC' : 1709, 'New York' : 2145, 'Dallas' : 2161},
'Chicago' : {'Minneapolis' : 661, 'Washington DC' : 1145, 'Boston' : 1613},
'Minneapolis' : {'Chicago' : 661, 'Denver' : 1483, 'Dallas' : 1532, 'Seattle' : 2661},
'Dallas' : {'Denver' : 1258, 'Minneapolis' : 1532, 'Las Vegas' : 1983, 'Washington DC' : 2113, 'Miami' : 2161},
'Denver' : {'Las Vegas' : 1225, 'Dallas' : 1258, 'Minneapolis' : 1483, 'Seattle' : 2161},
'Seattle' : {'San Francisco' : 1306, 'Denver' : 2161, 'Minneapolis' : 2661},
'San Francisco' : {'Los Angeles' : 629, 'Las Vegas' : 919, 'Seattle' : 1306},
'Las Vegas' : {'Los Angeles' : 435, 'San Francisco' : 919, 'Denver' : 1225, 'Dallas' : 1983},
'Los Angeles' : {'Las Vegas' : 435, 'San Francisco' : 629}
}

#taking input from the user

print("Different cities present in our network are ")
print("'Boston', 'New York' ,'Washington DC' ,'Miami' ,'Chicago' ,'Minneapolis', 'Dallas', 'Denver', 'Seattle', 'San Francisco', 'Las Vegas', 'Los Angeles'")
print("Please enter city name exactly as mentioned in the network as the program is case sensitive")
start = raw_input("Please enter the starting point")
if(str(start) == "San Francisco" or str(start)  == "Seattle" or str(start) == "Los Angeles"):
    DestGoods = raw_input(("Please enter the Destination of your goods"))
    print(" This is based on Distance that shortest distance to the city is calculated")
    dijkstra(nodes, distances, start)
    dijkstra_shortest(distances, start, DestGoods)

else:
    WestCoastBound = raw_input("Destination is WestCoast? (San Francisco/Seattle/Los Angeles- Y or N").upper()

    if WestCoastBound == 'Y':
        TypeOfSort = raw_input("Please enter the type of sorting: Cost or Distance").lower()
        # based on type of sort the appropriate function is calle
        if TypeOfSort == 'distance':
            least_city = djAlgo(nodes, distances, start)
            dijkstra_shortest(distances, start, least_city)
        elif TypeOfSort == 'cost':
            djAlgoCost(nodes, distances, start)
    else:

        DestGoods = raw_input(("Please enter the Destination of your goods"))
        print(" This is based on Distance that shortest distance to the city is calculated")
        dijkstra(nodes, distances, start)
        dijkstra_shortest(distances, start, DestGoods)








