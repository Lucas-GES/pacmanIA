graph = {"A":["D","C","B"],
            "B":["E"],
            "C":["G","F"],
            "D":["H"],
            "E":["I"],
            "F":["J"]}

graph2 = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}

def dfs_non_recursive(graph, source):

    if source is None or source not in graph:

        return "Invalid input"

    path = []

    stack = [source]

    while(len(stack) != 0):

        s = stack.pop()

        if s not in path:

            path.append(s)

        if s not in graph:

            #leaf node
            continue

        for neighbor in graph[s]:

            stack.append(neighbor)

    return " ".join(path)

def recursive_dfs(graph, source,path = []):

    if source not in path:

        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[source]:

            path = recursive_dfs(graph, neighbour, path)

    print(path)
    return path

DFS_path = dfs_non_recursive(graph, "A")

print(DFS_path)

path = recursive_dfs(graph2, "A")

print(" ".join(path))

movimentos = ["a","d","w","s"]
move = ""
for i in movimentos:    
    move += i 
print(movimentos)
print(move)