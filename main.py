move = input("vvedite hod konёm")
move = move.upper()
if (len(move)) == 5:
    k1, k2 = move.split('-')
    print(k1, k2 )
    if k1[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k1[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("ERROR")
    if k2[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or k2[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("ERROR")
else:
    #print(k1, k2 ,'YES')
    print('ERROR')
#проверку правильности хода нужно переделать!
if move in (k1,k2 ):
    print(k1, k2 ,'YES')
else:
    print(k1, k2 ,'NO')
