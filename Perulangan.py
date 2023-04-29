"""
program perulangan membaca buku
"""

jumlah_buku = 10
print("Ibu berkata membaca semua buku")

jumlah_buku_yangdibaca = 0

for jumlah_buku_yangdibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yangdibaca} sudah dibaca")


print(jumlah_buku_yangdibaca)