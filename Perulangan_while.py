"""
Program perulangan dengan while
"""

jumlah_buku = 10
print("Ibu Berkata baca semua buku mu")


jumlah_buku_yangdibaca = 0
print(f'Jumlah buku yang sudah di baca {jumlah_buku_yangdibaca}')

while jumlah_buku_yangdibaca < jumlah_buku:
    jumlah_buku_yangdibaca = jumlah_buku_yangdibaca + 1
    print(f"Buku ke {jumlah_buku_yangdibaca} sudah dibaca")


print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yangdibaca}')