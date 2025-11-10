class kalkulator:
    
    def _init_(self,nilai_awal):
        self.nilai = nilai_awal
        
    def tambah(self,angka):
        self.nilai += angka
        return self.nilai
    
    @staticmethod
    def kali(a,b):
        return a * b
    
calc = kalkulator(10)
print(f"Hasil tambah: {calc.tambah(5)}")

print(f"Hasil kali: {kalkulator.kali(5, 3)}")