def symbolsToIntCoord(k: str) -> (int, int):
    a = ord(k[0]) - ord('A') + 1
    b = int(k[1])
    return (a, b)


def isKnightJump(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1) or (
            abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2)


# move = input("vvedite hod konёm")
# move = move.upper()


def hodKonem(move):
    move = move.upper()
    if (len(move)) == 5:
        if move[2] != '-':
            return 'ERROR'
        k1, k2 = move.split('-')
        if len(k1) != 2 or len(k2) != 2:
            return 'ERROR'

        if k1[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k1[1] not in ["1", "2", "3", "4", "5", "6", "7",
                                                                                  "8"]:
            return "ERROR"
        if k2[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k2[1] not in ["1", "2", "3", "4", "5", "6", "7",
                                                                                  "8"]:
            return "ERROR"

        point1 = symbolsToIntCoord(k1)
        point2 = symbolsToIntCoord(k2)
        print(point1, point2)

        if (isKnightJump(point1, point2)):
            return 'YES'
        else:
            return 'NO'
    else:
        # print(k1, k2 ,'YES')
        return 'ERROR'

    # verhnee pravo /2 vverh,1 vpravo
    # verhnee levo /2 vverh,-1 vpravo
    # praviy verh /1 vverh,2 vpravo
    # praviy niz/-1 vverh,2 vpravo
    # niznie levo/-2 vverh,-1 vpravo
    # niznie pravo/-2 vverh,1 vpravo
    # leviy verh/1 vverh,-2 vpravo
    # leviy niz/-1 vverh,-2 vpravo


# if point2[0] == point1[0] + 1 and point2[1] == point1[1] + 2:
#    print('verhnee pravo')

# if point2[0] == point1[0] - 1 and point2[1] == point1[1] + 2:
#  print('verhnee levo')

# if point2[0] == point1[0] + 2 and point2[1] == point1[1] + 1:
#  print('praviy verh')

#   if point2[0] == point1[0] + 2 and point2[1] == point1[1] - 1:
#      print('praviy niz')

# if point2[0] == point1[0] - 2 and point2[1] == point1[1] - 1:
#    print('niznie levo')

# if point2[0] == point1[0] + 1 and point2[1] == point1[1] - 2:
#    print('niznie pravo')

#  if point2[0] == point1[0] - 2 and point2[1] == point1[1] + 1:
#    print('leviy verh')

# if point2[0] == point1[0] - 2 and point2[1] == point1[1] - 1:
# print('leviy niz')


with open('INPUT.TXT', 'r') as input:
    with open('OUTPUT.TXT', 'w') as output:
        output.write(hodKonem(input.readline().strip()))
