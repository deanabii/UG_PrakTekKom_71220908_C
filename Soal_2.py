print("Pemeriksa Kelipatan 9")

angka = int(input("Masukkan Kelipatan 9 yang ingin diperiksa:"))

def kelipatan_sembilan():
    kel = angka % 9
    return kel

if kelipatan_sembilan() == 0:
    print("Benar")
else:
    print("Salah")