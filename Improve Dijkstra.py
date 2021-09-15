import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 설정한 값 --> 10억으로 설정


n, m = map(int, input().split()) # n,m 입력 n = 노드의 갯수 , m = 간선의 갯수 입력

start = int(input()) # 시작 노드를 입력

graph = [[] for i in range(n + 1)] # 노드에 대한 정보를 가지고 있는 리스트 만들기

visited = [False] * (n + 1)  # 방문 한적이 있는지 체크하기 위한 리스트 만들기

distance = [INF] * (n + 1) # 최단거리 테이블을 무한대로 초기화


for _ in range(m):
    a, b, c = map(int, input().split()) # 모든 간선 정보를 입력받기

    graph[a].append((b, c)) # a번 노드에서 b번 노드로 가는 비용 == c번 노드4

def dijkstra(start):
    dijkstra(start)  # 다익스트라 알고리즘을 수행

    for i in range(1, n + 1):  # 최단 거리를 출력

        if distance[i] == INF:  # 노드에 도달할 수 없을 때
            print("INFINITY")

        else:  # 도달할 수 있다면
            print(distance[i])

def dijkstra(start):

    q = []
    heapq.heappush(q,(0,start)) # 시작노드를 0으로 설정하여 큐에 삽입
    distance[start] = 0

    while q: # q가 비어있지 않다면
        dist,now = heapq.heappop(q) # 가장 거리가 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist: # 현재 노드가 이미 처리됬으면 무시
            continue

        for i in graph[now]: # 인접한 노드들 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재의 노드를 거쳐서 다른 노드로 이동한 거리가 더 짧을 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start) # 다익스트라 알고리즘을 수행

for i in range(1, n + 1): # 최단 거리를 출력

    if distance[i] == INF: # 노드에 도달할 수 없을 때
        print("INFINITY")

    else: # 도달할 수 있다면
        print(distance[i])