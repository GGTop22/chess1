def symbolsToIntCoord(k: str) -> (int, int):
    a = ord(k[0]) - ord('A') + 1
    b = int(k[1])
    return (a, b)


def isKnightJunp(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1) or (abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2)


move = input("vvedite hod konёm")
move = move.upper()
if (len(move)) == 5:
    k1, k2 = move.split('-')
    print(k1, k2)
    if k1[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k1[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("ERROR")
    if k2[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k2[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("ERROR")

    point1 = symbolsToIntCoord(k1)
    point2 = symbolsToIntCoord(k2)
    print(point1, point2)
    point1 = symbolsToIntCoord(k1)
    point2 = symbolsToIntCoord(k2)
    print(point1, point2)

    if (isKnightJunp(point1, point2)):
        print('YES')
    else:
        print('NO')
else:
    # print(k1, k2 ,'YES')
    print('ERROR')


# verhnee pravo /2 vverh,1 vpravo
# verhnee levo /2 vverh,-1 vpravo
# praviy verh /1 vverh,2 vpravo
# praviy niz/-1 vverh,2 vpravo
# niznie levo/-2 vverh,-1 vpravo
# niznie pravo/-2 vverh,1 vpravo
# leviy verh/1 vverh,-2 vpravo
# leviy niz/-1 vverh,-2 vpravo

if point2[0] == point1[0] + 1 and point2[1] == point1[1] + 2:
    print('verhnee pravo')

if point2[0] == point1[0] - 1 and point2[1] == point1[1] + 2:
    print('verhnee levo')

if point2[0] == point1[0] + 2 and point2[1] == point1[1] + 1:
    print('praviy verh')

if point2[0] == point1[0] + 2 and point2[1] == point1[1] - 1:
    print('praviy niz')

if point2[0] == point1[0] - 2 and point2[1] == point1[1] - 1:
    print('niznie levo')

if point2[0] == point1[0] + 1 and point2[1] == point1[1] - 2:
    print('niznie pravo')

if point2[0] == point1[0] - 2 and point2[1] == point1[1] + 1:
    print('leviy verh')

if point2[0] == point1[0] - 2 and point2[1] == point1[1] - 1:
    print('leviy niz')
