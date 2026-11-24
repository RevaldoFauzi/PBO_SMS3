class Mahasiswa :
    nim = 14022500058
    nama = "Revaldo Fauzi"

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {self.nama}, nama saya {nama}")

mahasiswa = Mahasiswa ()
mahasiswa.nama = "Revaldo Fauzi"
mahasiswa.perkenalan()
mahasiswa.hello("Alex")
