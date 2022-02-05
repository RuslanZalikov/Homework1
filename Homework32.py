import math
from pprint import pprint

symbol = 'ABCDEFGH'

def spiderVsFly(Spider, Fly):
    inputData = [Spider, Fly]
    K = math.sqrt(2*(1 - math.cos(math.pi/4)))
    Fisrt_shortest_way = math.inf
    Second_shortest_way = math.inf
    OutputData = []
    if inputData[0][0] == inputData[1][0]:
        Fisrt_shortest_way = abs(int(inputData[0][1]) - int(inputData[1][1]))
        OutputData = list(range(min(int(inputData[0][1]), int(inputData[1][1])),max(int(inputData[0][1]), int(inputData[1][1])) + 1))
        if int(inputData[0][1]) > int(inputData[1][1]):
            OutputData.reverse()
        OutputData = [inputData[0][0] + str(i) for i in OutputData]
        return OutputData
    else:
        Fisrt_shortest_way = int(inputData[0][1]) + int(inputData[1][1])
        Second_shortest_way = abs(int(inputData[0][1]) - int(inputData[1][1])) + min(int(inputData[0][1]), int(inputData[1][1]))*K*min(abs(ord(inputData[0][0]) - ord(inputData[1][0])), 8 - abs(ord(inputData[0][0]) - ord(inputData[1][0])))
        if Fisrt_shortest_way <= Second_shortest_way:
            OutputData += list(range(int(inputData[0][1]) + 1))
            OutputData.reverse()
            OutputData = [inputData[0][0] + str(i) for i in OutputData]
            OutputData[-1] = 'A0'
            OutputData += [inputData[1][0] + str(i) for i in list(range(1, int(inputData[1][1]) + 1)) if inputData[0][0] not in str(i)]
            return OutputData
        else:
            if int(inputData[0][1]) > int(inputData[1][1]):
                OutputData += list(range(int(inputData[1][1]), int(inputData[0][1]) + 1))
                OutputData.reverse()
                OutputData = [inputData[0][0] + str(i) for i in OutputData]
                OutputData += [chr((((ord(inputData[0][0]) + i + 1)-65)%8)+65) + str(inputData[1][1]) for i in range(min(abs(ord(inputData[0][0]) - ord(inputData[1][0])), 8 - abs(ord(inputData[0][0]) - ord(inputData[1][0]))))]
                return OutputData
            elif int(inputData[0][1]) < int(inputData[1][1]):
                if inputData[0][0] < inputData[1][0]:
                    OutputData += [chr((((ord(inputData[0][0]) - i) - 65) % 8) + 65) + str(inputData[0][1]) for i in range(min(abs(ord(inputData[0][0]) - ord(inputData[1][0])), 8 - abs(ord(inputData[0][0]) - ord(inputData[1][0]))))]
                else:
                    OutputData += [chr((((ord(inputData[0][0]) + i) - 65) % 8) + 65) + str(inputData[0][1]) for i in range(min(abs(ord(inputData[0][0]) - ord(inputData[1][0])), 8 - abs(ord(inputData[0][0]) - ord(inputData[1][0]))))]
                OutputData += [inputData[1][0] + str(i) for i in range(int(inputData[0][1]), int(inputData[1][1]) + 1)]
                return OutputData
            else:
                if inputData[0][0] < inputData[1][0]:
                    OutputData += [chr((((ord(inputData[0][0]) - i) - 65) % 8) + 65) + str(inputData[1][1]) for i in range(min(abs(ord(inputData[0][0]) - ord(inputData[1][0])), 8 - abs(ord(inputData[0][0]) - ord(inputData[1][0]))) + 1)]
                else:
                    OutputData += [chr((((ord(inputData[0][0]) + i) - 65) % 8) + 65) + str(inputData[1][1]) for i in range(min(abs(ord(inputData[0][0]) - ord(inputData[1][0])), 8 - abs(ord(inputData[0][0]) - ord(inputData[1][0]))) + 1)]
                return OutputData

Spider = input()
Fly = input()
Output = spiderVsFly(Spider, Fly)
print('-'.join(Output))