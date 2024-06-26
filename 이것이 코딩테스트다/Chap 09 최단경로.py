# import sys
# input =sys.stdin.readline
# INF=int(1e9)

# #노드의 개수, 간선의 개수를 입력받기

# #노드의 개수, 간선의 개수를 입력 받기
# n,m=map(int,input().split())

# # 시작 노드 번호를 입력 받기
# start=int(input())

# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# graph=[[] for i in range(n+1)]

# #방문한 적이 있는지 체크하는 목적의 리스트 만들기
# visited=[False]*(n+1)

# # 최단 거리 테에블을 모두 무한으로 초기화
# distance=[INF]*(n+1)

# # 모든 간선 정보를 입력받기

# for _ in range(m):
#     a,b,c=map(int,input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append((b,c))

# # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환

# def get_smallest_node():
#     min_value=INF
#     index=0 #가장 최단 거리가 짧은 노드(인덱스)
#     for i in range(1,n+1):
#         if distance[i]<min_value and not visited[i]:
#             min_value=distance[i]
#             index=i
#     return index

# def dijkstra(start):
#     # 시작 노드에 대해서 초기화
#     distance[start]=0
#     visited[start]=True
#     for j in graph[start]:
#         distance[j[0]]=j[1]
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    
#     for i in range(n-1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now=get_smallest_node()
#         visited[now]=True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost=distance[now]+j[1]

#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]]=cost

# dijkstra(start)
# # 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1,n+1):
#     # 도달할 수 없는 경우, 무한이라고 출력
#     if distance[i]==INF:
#         print("INFINITY")

#     # 도달할 수 있는 경우 거리를 출력
#     else:
#         print(distance[i])

# ### 9-2.py 개선된 다익스트라 알고리즘 소스코드

# import heapq
# import sys
# input=sys.stdin.readline
# INF=int(1e9)

# # 노드의 개수, 간선의 개수를 입력ㅂ다기
# n,m=map(int,input().split())

# # 시작 노드 번호를 입력 받기
# start=int(input())

# #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# graph=[[] for i in range(n+1)]

# # 최단 거리 테이블을 모두 무한으로 초기화
# distance=[INF]*(n+1)


# # 모든 간선 정보를 입력받기
# for _ in range(m):
#     a,b,c=map(int,input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append((b,c))


# def dijkstra(start):
#     q=[]
#     #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
#     heapq.heappush(q,(0,start))
#     distance[start]=0
#     while q: #큐가 비어있지 않다면
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         dist,now=heapq.heappop(q)

#         #현재 노드가 이미 처리된 적이 있는 노드라면 무시
#         if distance[now]<dist:
#             continue

#         #현재 노드와 연결된 다른 인접한 노드들을 확인
#         for i in graph[now]:
#             cost=dist+i[1]

#             #현재를 거쳐서, 다른 노드로 이동하는 거리가가 더 짧은 경우
#             if cost<distance[i[0]]:
#                 distance[i[0]]=cost
#                 heapq.heappush(q,(cost,i[0]))


# # 다익스트라 알고리즘을 수행
# dijkstra(start)

# # 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1,n+1):
#     # 도달할 수 없는 겨우, 무한(INFINITY)이라고 출력
#     if distance[i]==INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

#-----------------------------------------------------------------------#

# # 9-3.py 플로이드 워셜 알고리즘 소스코드

# INF=int(1e90) # 무한을 의미하는 값으로 10억을 설정

# # 노드의 개수 및 간선의 개수를 입력받기

# n=int(input())
# m=int(input())

# # 2차원 리스트(그래프 표현)를 만들고, 모든값을 무한으로 초기화
# graph=[[INF]*(n+1) for _ in range(n+1)]


# # 자기 자신에서 자기 자신으로 가는 비용으로 0으로 초기화
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if a==b:
#             graph[a][b]=0

# # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화

# for _ in range(m):
#     #A에서 B로 가는 비용은 C라고 설정
#     a,b,c=map(int,input().split())
#     graph[a][b]=c

# # 점화식에 따라 플로이드 워셜 알고리즘을 수행

# for k in rnage(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# # 수행된 결과를 출력

# for a in range(1,n+1):
#     for b in range(1,n+1):
#         # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
#         if graph[a][b]==INF:
#             print("INFINITY",end=" ")
#         # 도달할 수 있는 경우 거리를 출력
#         else:
#             print(graph[a][b],end=" ")

#     print()


# # 9-4.py 미래 도시

# INF=int(1e9)

# node,edge=map(int, input().split())

# graph=[[INF]*(node+1)for _ in range(n+1)]

# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if a==b:
#             graph[a][b]=0

# # 각 간선에 대한 정보를 입력 받는다.

# for _ in range(edge):
#     # 서로 연결되어 있으면 1
#     n,m=map(int,input().split())
#     graph[n][m]=1
#     graph[m][n]=1

# # 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력 받기
# x,k=map(int, input().split())

# # 점화식에 따라 플로이드 워셜 알고리즘을 수핼



# # 9-5.py 실전문제 전보

# import heapq
# import sys
# input=sys.stdin.readline

# INF=int(1e9) # 무한을 의미하는 값으로 10억을 설정

# # 노드의 개수, 간선의 개수, 시작노드를 입력 받기
# n,m,start=map(int,input().split())

# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# graph=[[] for i in range(n+1)]

# # 최단 거리 테이블을 모두 무한으로 초기화
# distance=[INF]*(n+1)

# # 모든 간선 정보를 입력받기

# for _ in range(m):
#     x,y,z=map(int,input().split())
#     graph[x].append((y,z))

# def dijkstra(start):
#     q=[]
#     heapq.heappush(q,(0,start))
#     distance[start]=0
    
#     while q:
#         # 가장 최단 거리가 짧은 거리를 가지고 있는 노드 꺼내기
#         dist, node=heapq.heappop(q)
#         if distance[node]<dist:
#             continue

#         # 현재 노드와 연결된 다른 인접노드 찾기
#         for i in graph[node]:
#             cost= dist+i[1]
#             if cost<distance[i[0]]:
#                 distance[i[0]]=cost
#                 heapq.heappush(q,(cost,i[0]))


# dijkstra(start)

# # 도달할 수 있는 노드의 개수
# count=0

# # 도달할 수 있는 노드 중에서,가장 멀리 있는 노드와의 최단거리
# max_distance=0

# for d in distance:
#     # 도달할 수 있는 노드인 경우에만 카운트를 한다. 
#     if d!=INF:
#         count+=1
#         max_distance=max(max_distance,d)

# # 시작노드는 제외해야 하므오 count-1을 출력한다.
# print(count-1,max_distance)



# 10-1.py 기본적인 서로소 집합 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기

def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

# 두 원소가 속한 집합을 합치기

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b 

# 노드의 개수와 간선의 개수 입력 받기 
v,e=map(int,input().split())

parent()









        










