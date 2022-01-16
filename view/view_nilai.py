def tampilkan():
    if data.items():
        print("                   D  A  F  T  A  R      N  I  L  A  I                        ")
        print(" __________________________________________________________________________")
        print("| NO |     NAMA      |    NIM       | TUGAS  |  UTS  |  UAS  | NILAI AKHIR |")
        print("|----|---------------|--------------|--------|-------|-------|-------------|")
        i = 0
        for a in data.items():
            i += 1
            print(f"|{i:3} | {a[0]:12s}  |{a[1][0]:12}  |{a[1][1]:5d}   |{a[1][2]:4d}   |{a[1][3]:5d}  |{a[1][4]:8.2f}     |")
    else:
        print("                   D  A  F  T  A  R      N  I  L  A  I                     ")
        print(" __________________________________________________________________________")
        print("| NO |      NAMA     |      NIM     | TUGAS  |  UTS  | UAS  | NILAI AKHIR  |")
        print("|                                                                          |")
        print("|                           TIDAK  ADA  DATA                               |")
        print("|                                                                          |")
    print("|____|_______________|______________|________|_______|_______|_____________|")