from pprint import pprint
import math

def Generator(point, V):
    for j in range(len(V[point])):
        if V[point][j] >= 0:
             yield j

def Generator_Path_recovery(point, V):
    for j in range(len(V[point])):
        if V[point][j] > 0:
             yield j

def Path_recovery(Start, Finish, shortest_way, V):
    point = Finish
    short_with_point = dict()
    final_pyth = []
    while point != Start:
        min_value = math.inf
        for i in Generator_Path_recovery(point, V):
            short_with_point.update({i:shortest_way[i]+V[i][point]})
        for key in short_with_point:
            if short_with_point[key] <= min_value:
                min_value = short_with_point[key]
                min_index = key
        point = min_index
        short_with_point = dict()
        if Start%5 == 0 and point%5 == 0:
            return final_pyth
        if point%5 == 0:
            point = 0
        final_pyth.append(point)
    return final_pyth

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
                shortest_way[i] = min(shortest_way[i], V[point][i] + shortest_way[point])
        min_shortest_way = max(shortest_way)
        mini = -1
        for i in range(len(shortest_way)):
            if shortest_way[i] < min_shortest_way and i not in mark:
                min_shortest_way = shortest_way[i]
                mini = i
        point = mini
        if point >= 0:
            mark.append(point)
    return shortest_way

GRAF = [i+j for i in 'ABCDEFGH' for j in '01234']
GRAFi = [j+i*5 for i in range(8) for j in range(5)]
Translate = {GRAF[i]:GRAFi[i] for i in range(40)}
print(Translate)
ReverseTranslate = {GRAFi[i]:GRAF[i] for i in range(40)}
print(ReverseTranslate)
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
Spider = input()
Fly = input()
Spider = Translate[Spider]
Fly = Translate[Fly]
s = Dijkstra(Spider,V)
s = Path_recovery(Spider, Fly, s, V)
s.reverse()
for i in range(len(s)):
    s[i] = ReverseTranslate[s[i]]
s.append(ReverseTranslate[Fly])
print('-'.join(s))