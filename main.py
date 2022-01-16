data = {}

def tambah():
    print("◆ T A M B A H   D A T A ◆")
    nama = input("N a m a\t\t: ")
    nim = int(input("N I M\t\t: "))
    tugas = int(input("Nilai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = nim, tugas, uts, uas, nilaiakhir


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


def hapus():
    print("◆ H A P U S   D A T A ◆ ")
    nama = input(" Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("`````````````````````````````````")
        print("‰‰‰| BERHASIL MENGHAPUS DATA |‰‰‰")
        print("`````````````````````````````````")
    else:
        print("¡¡¡ DATA ~{0}~ TIDAK ADA ¡¡¡".format(nama))


def ubah():
    print()
    print("◆ U B A H    D A T A ◆")
    print()
    nama = input("Masukan Nama\t\t: ")
    if nama in data.keys():
        nim = input("NIM Baru\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("====== BERHASIL  MENGUBAH  DATA ======")
        print()
    else:
        print("¡¡¡ DATA ~{0}~ TIDAK ADA ¡¡¡".format(nama))

while True:
    print()
    print("============ D A T A   M A H A S I S W A  ===============")
    print()
    x = input("1.| Tambah \n2.| Tampilkan \n3.| Hapus Data \n4.| Ubah Data\nJawab: ")
    if x.lower() == "1":
        tambah()
    elif x.lower() == "2":
        tampilkan()
    elif x.lower() == "3":
        hapus()
    elif x.lower() == "4":
        ubah()
    elif x.lower() == "0":
        print()
        print("◆◆◆   K E L U A R   D A R I   P R O G R A M   ◆◆◆")
        print()
        break