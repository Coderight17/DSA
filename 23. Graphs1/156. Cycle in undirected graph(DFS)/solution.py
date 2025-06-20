#The problem is to find if an undirected graph has a cycle or not
def dfs_visit(graph,visited,u,parent):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            dfs_visit(graph,visited, v, u)
        else:
            if v != parent:
                return True
    return False
graph = {0: {1,2}, 1: {0,4}, 2: {0, 3,5}, 3:{2}, 4:{1,6}, 5:{2,6}, 6:{4,5}}
# graph = {0:{}, 1:{2}, 2:{1, 3}, 3:{2}}
n = int(input('Enter the no of vertices : '))
visited = [False]*n
fg7 = False
for i in graph:
    if not visited[i]:
       fg =  dfs_visit(graph,visited,i, None)
       if fg:
           fg7 = True
           print('Cycle detected')
           break
if not fg7:
    print('No cycle detected.')
