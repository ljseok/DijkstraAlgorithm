import sys
input = sys.stdin.readline
<<<<<<< HEAD
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
=======
INF = int(1e9) # 무한의 값으로 10억을 설정

n,m = map(int, input().split()) # 노드의 갯수, 간선의 갯수 입력받기
st = int(input()) # 시작노드 입력
gra = [[] for i in range(n+1)] # 각 노선의 정보를 담는 리스트
visit = [False] * (n+1) # 방문을 체크하는 리스트
dist = [INF] * (n+1) # 최단거리 테이블은 무한의 값으로 초기화

for _ in range(m):
    a,b,c = map(int, input().split()) # 모든 간선의 정보 입력 , a부터 b까지 가는 비용이 c
    gra[a].append((b,c))

def small_node(): # 가장 거리가 짧은 노드를 계산
    min = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1,n+1):
        if dist[i] < min and not visit[i]:
            min = dist[i]
            index = i
    return index

def dijkstra(st): # 다익스트라 알고리즘
    dist[st] = 0
    visit[st] = True
    for j in gra[st]:
        dist[j[0]] = j[1]

    for i in range(n-1): # 시작노드를 제외한 n-1개의 노드를 반복
        now = small_node() # 최단거리가 가장 짧은 노드를 꺼내서
        visit[now] = True # 방문처리

        for j in gra[now]: # 현재노드와 연결된 노드들을 확인
           # cost = dist[now] + j[1]
            if dist[now] + j[1] < dist[j[0]]: # 현재노드를 거쳐서 가는 경우가 원래 노드보다 짧은 경우
                dist[j[0]] = dist[now] + j[1] # 거쳐간 노드를 최단 거리로 갱신

dijkstra(st)

for i in range(1,n+1):
    if dist[i] == INF: # 도달할 수 없는 경우
        print("INFINITY")
    else: # 도달할 수 있는 경우
        print(dist[i])

>>>>>>> 09d4728 (기본적인 다익스트라 알고리즘)





