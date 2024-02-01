

''' creating a following graph 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['E', 'A'],
    'E': [],
}'''
def add_nodes(node1,node2,graph):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)

    return graph

def find_path(graph,start,end,path =[]):
    path = path + [start]
    if start == end:
        return start
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            print("path",path)
            if newpath:
                return newpath


def bfs(graph,visited,node,queue):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s ," ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def dfs(graph,visited,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,visited,neighbour)



def create_graph():
    graph = dict()
    graph = add_nodes("A","B",graph)
    graph = add_nodes("A","C",graph)
    graph = add_nodes("D","E",graph)
    graph = add_nodes("C","D",graph)
    graph = add_nodes("D","A",graph)
    graph = add_nodes("B","D",graph)
    graph = add_nodes("B","E",graph)
    return (graph)
    

graph = create_graph()
# print(find_path(graph,"A","D"))
print(bfs(graph,[],"A",[]))
print(dfs(graph,set(),"A"))
