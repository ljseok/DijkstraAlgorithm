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
    graph[a].append((b, c)) # a번 노드에서 b번 노드로 가는 비용 == c번 노드

def get_smallest_node(): # 방문하지 않은 노드들 중에서 가장 짧은 노드를 반환하는 함수
    min_value = INF
    index = 0 # 가장 거리가 짧은 노드
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작노드를 0으로 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1): # 시작노드를 제외한 n-1개의 노드를 반복
        now = get_smallest_node() # 지금 최단거리가 가장 짧은 노드를 꺼내서 방문처리를 한다
        visited[now] = True

        for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인한다
            cost = distance[now] + j[1]

            if cost < distance[j[0]]: # 현재노드를 통과해서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start) # 다익스트라 알고리즘을 수행

for i in range(1, n + 1): # 최단 거리를 출력
    if distance[i] == INF: # 노드에 도달할 수 없을 때
        print("INFINITY")
    else: # 도달할 수 있다면
        print(distance[i])





