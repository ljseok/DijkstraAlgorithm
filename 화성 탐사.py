import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한의 값으로 10억 설정

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for test in range(int(input())): # 테스트 케이스 까지 반복
    n = int(input()) # 노드의 갯수 입력받기

    graph = []

    for i in range(n):
        graph.append(list(map(int,input().split()))) # 맵 정보 입력

    distance = [[INF] * n for _ in range(n)] # 최단거리를 무한의 값으로 초기화

    x,y = 0,0 # 시작위치 0,0 설정
    q = [(graph[x][y],x,y)]
    distance[x][y] = graph[x][y]

    while q:
        dist,x,y = heapq.heappop(q)

        if distance[x][y] < dist: # 이미 처리된 적이 있다면
            continue # 무시
        for i in range(4): # 인접한 4가지 방향을 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 맵을 벗어나게 되면
                continue # 무시
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]: # 노드를 거쳐간 경우가 더 짧으면
                distance[nx][ny] = cost # 최단거리 갱신
                heapq.heappush(q,(cost,nx,ny))
    print(distance[n-1][n-1]) # 출력
