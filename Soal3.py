print("===== Selamat Datang Di XXV =====")
input("Masukkan tanggal Hari Ini: ")
print(" == Berikut Genre Film Yang Tersedia == \n1. Horror \n2. Action ")
a = int(input("Silahkan Pilih Mau nonton film bergenre apa: "))
if a == 1:
    kamu = [' horror']
    konversi = set(kamu)
    
elif a == 2:
    minuman = [' Action ']
    konversi = list(minuman)

print('pilihan yang anda pilih tidak tersedia di bioskop ini')

