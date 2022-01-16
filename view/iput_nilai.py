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