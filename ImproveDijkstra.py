import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(st):
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

for i in range(1,n+1): # 최단거리 출력
    if distance[i] == INF: # 도달할 수 있는 경우
        print("INFINITY")
    else: # 도달할 수 없는 경우
        print(distance[i])

