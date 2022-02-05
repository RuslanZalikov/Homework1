from pprint import pprint
import math

def Generator(point, D):
    for j in range(len(D[point])):
        if D[point][j] >= 0:
             yield j

def Dijkstra(point, V):
    shortest_way = [math.inf]*len(V)
    shortest_way[point] = 0
    pyth = [0] * len(V)
    for i in range(len(V)):
        pyth[i] = []*len(V)
    mark = [point]
    while point != -1:
        for i in Generator(point, V):
            if i not in mark:
                if shortest_way[i] > V[point][i] + shortest_way[point]:
                    shortest_way[i] = V[point][i] + shortest_way[point]
                    pyth[i].append(point)

                # shortest_way[i] = min(shortest_way[i], V[point][i] + shortest_way[point])
        min_shortest_way = max(shortest_way)
        mini = -1
        for i in range(len(shortest_way)):
            if shortest_way[i] < min_shortest_way and i not in mark:
                min_shortest_way = shortest_way[i]
                mini = i
        point = mini
        if point >= 0:
            mark.append(point)

    # return shortest_way
    return pyth

GRAF = [i+j for i in 'ABCDEFGH' for j in '01234']
GRAFi = [j+i*5 for i in range(8) for j in range(5)]
for i in range(40):
    print(GRAF[i], ' ', GRAFi[i])
V = [-1] * len(GRAF)
for i in range(len(GRAF)):
    V[i] = [int(-1)] * len(GRAF)
for i in range(len(GRAF)):
    for j in range(len(GRAF)):
        if GRAF[i][1] == GRAF[j][1] and (abs(ord(GRAF[i][0]) - ord(GRAF[j][0])) == 1 or (GRAF[i][0] in 'AH' and GRAF[j][0] in 'AH')):
            V[i][j] = math.sqrt(int(GRAF[i][1])**2 + int(GRAF[j][1])**2 - 2*int(GRAF[i][1])*int(GRAF[j][1])*math.cos(math.pi/4))
        if '0' in GRAF[i] and '1' in GRAF[j]:
            V[i][j] = 1
        if '0' in GRAF[i] and '0' in GRAF[j]:
            V[i][j] = 0
        if abs(int(GRAF[i][1]) - int(GRAF[j][1])) == 1 and GRAF[i][0] == GRAF[j][0]:
            V[i][j] = 1
    V[i][i] = 0
for i in range(len(GRAF)):
    for j in range(len(GRAF)):
        print(V[i][j], end=' ')
    print()
print()
print()
print()
print()
s = Dijkstra(0,V)
# print(s)
for i in s:
    print(i)