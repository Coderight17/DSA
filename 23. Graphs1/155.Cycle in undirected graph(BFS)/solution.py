#The task is to find if a cycle exists in an undirected graph using bfs
def bfs(graph,visited,u):
    queue = [[u, None]]
    while queue:
        element = queue.pop(0)
        s = element[0]
        parent = element[1]
        for v in graph[s]:
            if not visited[v]:
                visited[v] = True
                queue.append([v,s])
            else:
                if v != parent:
                    return True
    return False
n = int(input('Enter the no of vertices.'))
graph = {0: {1,2}, 1: {0,4}, 2: {0, 3,5}, 3:{2}, 4:{1,6}, 5:{2,6}, 6:{4,5}}
visited = [False]*n
fg7 = False
for i in range(n):
    if not visited[i]:
        fg = bfs(graph, visited, i)
        if fg:
            fg7 = True
            print('Cycle detected')
            break
if not fg7:
    print('Cycle not detected.')
