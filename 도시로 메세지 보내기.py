import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한의 값으로 10억을 설정

n,m,start = map(int,input().split()) # n = 노드의갯수 , m = 간선의 갯수 , start = 시작노드

graph=[[] for i in range(n+1)] # 노드이 정보를 담고있는 리스트 만들기

distance =[INF] * (n+1) # 최단 거리 테이블을 무한대로 초기화

for _ in range(m):
    x, y, z = map(int, input().split()) # 모든 간선의 정보를 입력받기
    graph[x].append((y,z)) # x에서 출발하여 y에 도착할 때 까지의 비용

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start)) # 시작노드로 가기위한 최단 경로를 0으로 설정하여 큐에 삽입한다
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        dist,now = heapq.heappop(q) # 가장 최단거리가 짧은 노드를 꺼내기

        if distance[now] < dist: # 현재노드가 이미 처리되었다면
            continue # 무시

        for i in graph[now]: # 현재노드와 인접한 노드들을 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start) # 디익스트라 알고리즘을 수행

count = 0 # 도달할 수 없는 노드의 갯수를 0으로 초기화
max_distance = 0 # 도달할 수 없는 노드중에서 가장 가까운 거리를 0으로 초기화

for d in distance:
    if d !=INF : # 도달할수 있는 경우
        count += 1 # 카운트 값을 1 증가시키고
        max_distance = max(max_distance,d) # d, 가장가까운거리랑 비교해서 더 큰값을 삽입

print(count-1, max_distance)






