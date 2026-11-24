class Sekolah:
    pass

class Siswa:
    pass

Bapa_budi= Sekolah()
Revaldo = Siswa()

print(type(Bapa_budi))
print(type(Revaldo))



Sir_Revaldo = Sekolah()
Bapa_budi = Siswa()


print(type(Sir_Revaldo))
print(type(Bapa_budi))

Kepala_sekolah = Sekolah()
Kepala_sekolah.umur = 36
Kepala_sekolah.nama = "Sir_Valdo"

print(Kepala_sekolah.umur)
print(Kepala_sekolah.nama)

Orang_tua = Siswa()
Orang_tua.umur = 59
Orang_tua.nama = "Budi"

print(Orang_tua.umur)
print(Orang_tua.nama)