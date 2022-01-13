import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 시작노드로 가기위한 최단경로를 0으로 설정하여 큐에삽입
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q) # 큐 꺼내기

        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있다면
            continue # 무시
        for i in graph[now]: # 인접한 노드들을 확인하면서
            if dist + i[1] < distance[i[0]]: # 현재노드를 거쳐간 최단거리가 더 짧은 경우
                distance[i[0]] = dist + i[1] # 노드를 거쳐간 거리로 최단거리를 갱신
                heapq.heappush(q,(dist+i[1], i[0]))
dijkstra(start)

cnt = 0 # 도달할 수 있는 노드의 갯수
max_dist = 0 # 도달할 수 있는 노드 중에서 가장멀리 떨어진 노드와의 최단거리

for i in distance:
    if i != INF: # 도달할 수 있는 경우
        cnt += 1
        max_dist = max(max_dist,i)

print(cnt-1, max_dist) # 도시의 갯수와 걸리는 시간 출력











