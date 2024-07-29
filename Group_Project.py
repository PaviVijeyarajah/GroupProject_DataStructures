#Group Project
#Pavi Vijeyarajah
#100874494
#July 24 2024
import heapq

#This function extracts the charging_station.txt and makes it to a dictionary
def file(file):
    graph={}
    with open(file) as input_file:
        for line in input_file: #Reads each line of the txt file
            node,edge = line.split(':') #uses the colon to split it into nodes and edges 
            node = node.strip().strip("'") #Removes the whitespaces and single quotations from node
            edge = eval(edge.strip()) 
            graph[node] = edge # Puts the nodes and edges into the graph dictionary
    return graph

def dijikstra(graph,start):
    distances={}
    for node in graph: #Loop to set distance of each node to infinity
        distances[node] = float('inf')
    distances[start] = 0 #Set the starting node distance to 0
    queue = [(0, start)]

    while queue: #priority queue while loop that stops when queue is empty
        current_distance, current_node = heapq.heappop(queue) #pops the node with the smallest distance
        for neighbor, weight in graph[current_node]: 
            distance = current_distance + weight #Calculate the distance of neighbours
            if distance < distances[neighbor]: #Check for shorter path
                distances[neighbor] = distance #Update shortest distance
                heapq.heappush(queue, (distance, neighbor)) #Push updated distance and neighbor in queue
    return distances


graph=file("charging_station.txt")

shortest_paths = dijikstra(graph, "A")

#Dijikstra algorithm UI
while True:
    print()
    choice=input("Pick a charging station you would like to find the shortest path for (H,K,Q,T)\nType the letter of the charging station or exit to leave: ")
    if choice=="exit":
        break
    for node, dist in shortest_paths.items():#Loops through each distance to find a certain shortest path
        if node==choice:
            print("From starting point A the distance to", node," is ",dist)
