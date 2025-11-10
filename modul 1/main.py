# TUGAS PRAKTIKUM MODUL 1
class PersegiPanjang:
    # Constructor dengan parameter panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


# Membuat object dari class PersegiPanjang
pp1 = PersegiPanjang(10, 5)
pp2 = PersegiPanjang(7, 3)

# Menampilkan hasil perhitungan
print("Persegi Panjang 1")
print("Panjang:", pp1.panjang)
print("Lebar:", pp1.lebar)
print("Luas:", pp1.hitung_luas())
print("Keliling:", pp1.hitung_keliling())

print("\nPersegi Panjang 2")
print("Panjang:", pp2.panjang)
print("Lebar:", pp2.lebar)
print("Luas:", pp2.hitung_luas())
print("Keliling:", pp2.hitung_keliling())