def symbolsToIntCoord(k: str)->(int, int):
    a = ord(k[0])-ord('A')+1
    b = int(k[1])
    return (a,b)

move = input("vvedite hod konёm")
move = move.upper()
if (len(move)) == 5:
    k1, k2 = move.split('-')
    print(k1, k2)
    if k1[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k1[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("ERROR")
    if k2[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k2[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("ERROR")

    point1 =     symbolsToIntCoord(k1)
    point2 =     symbolsToIntCoord(k2)
    print (point1, point2)
else:
    # print(k1, k2 ,'YES')
    print('ERROR')
# проверку правильности хода нужно переделать!
if move in (k1, k2):
    print(k1, k2, 'YES')
else:
    print(k1, k2, 'NO')


# verhnee pravo /2 vverh,1 vpravo
# verhnee levo /2 vverh,-1 vpravo
# praviy verh /1 vverh,2 vpravo
# praviy niz/-1 vverh,2 vpravo
# niznie levo/-2 vverh,-1 vpravo
# niznie pravo/-2 vverh,1 vpravo
# leviy verh/1 vverh,-2 vpravo
# leviy niz/-1 vverh,-2 vpravo
