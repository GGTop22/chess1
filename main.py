move = input("vvedite hod konёm")
if (len(move)) == 5:
    k1, k2 = move.split('-')
    print(k1, k2)
else:
    print('ERROR')
