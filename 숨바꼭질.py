import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) # 헛간의 갯수, 양방향 통로 입력받기
start = 1
graph = [[] for i in range(n+1)] # 노드에 대한 정보를 가지고 있는 리스트 만들기
distance = [INF] * (n+1) # 최단거리 테이블을 무한대로 초기화

for _ in range(m):
    a,b = map(int,input().split()) # 헛간의 정보 입력받기
    graph[a].append((b,1)) # a,b 헛간의 이동비용이 1
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: # 노드가 이미 처리되었다면
            continue # 무시

        for i in graph[now]: # 인접한 노드들을 확인하면서
            if dist + i[1] < distance[i[0]]:  # 현재노드를 거쳐간 최단거리가 더 짧은 경우
                distance[i[0]] = dist + i[1]  # 노드를 거쳐간 거리로 최단거리를 갱신
                heapq.heappush(q,(dist + i[1], i[0]))

dijkstra(start)

max_node = 0 # 최단거리가 가장 먼 노드
max_dist = 0 # 도달할 수 있는 노드중에서 거리가 가장 먼 노드
result = []

for i in range(1,n+1):
    if max_dist < distance[i]: # 현재거리가 최단거리가 가장 먼 노드보다 더 멀리있을 경우
        max_node = i
        max_dist = distance[i]
        result = [max_node]
    elif max_dist == distance[i]: # 현재거리가 최단거리가 가장 먼 노드랑 동일한 경우
        result.append(i)
print(max_node,max_dist,len(result)) # 헛간번호, 헛간 사이의 거리, 헛간의 갯수 출력

