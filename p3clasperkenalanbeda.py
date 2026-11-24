class Mahasiswa:
    nim = 14022500058
    nama = "Valdo"

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim



mhs = Mahasiswa("Valdo","14022500058")
print(mhs.nama)
print(mhs.nim)
