print("=================")
print("1. Jumlah    [+]")
print("2. Kurang    [-]")
print("3. Kali      [*]")
print("4. Bagi      [/]")
print("=================")

pilih = input("Pilih operasi (1/2/3/4):")
print("=================")
bil1 = eval(input("Masukkan bilangan pertama:"))
bil2 = eval(input("Masukkan bilangan kedua:"))

def penjumlahan(bil1,bil2):
        jmlh = bil1 + bil2
        return jmlh
def pengurangan(bil1,bil2):
        krg = bil1 - bil2
        return krg
def perkalian(bil1,bil2):
        kali = bil1 * bil2
        return kali 
def pembagian(bil1,bil2):
        bagi = bil1 / bil2
        return bagi

if pilih == "1":
    print("Hasil operasi dari",bil1,"+",bil2,"=",penjumlahan(bil1,bil2))
   
elif pilih == "2":
    print("Hasil operasi dari",bil1,"-",bil2,"=",pengurangan(bil1,bil2))
   
elif pilih == "3":
    print("Hasil operasi dari",bil1,"*",bil2,"=",perkalian(bil1,bil2))
    
elif pilih == "4":
    print("Hasil operasi dari",bil1,"/",bil2,"=",pembagian(bil1,bil2))
    




