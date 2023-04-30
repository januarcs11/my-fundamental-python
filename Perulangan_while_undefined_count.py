"""
Program perulangan dengan while
"""

buku = 10
print("Ibu Berkata baca semua buku mu")
jumlah_baca = 0

jumlah_pahami = 0
print(f'Jumlah buku yang sudah di baca dan di pahami {jumlah_pahami}')


while jumlah_baca < buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_pahami == 9:
        print(f"Buku ke {jumlah_pahami + 1} belum paham ")
    else:
        jumlah_pahami = jumlah_pahami + 1
        print(f"Buku ke {jumlah_pahami} sudah dibaca dan di pahami")
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_pahami}')
if jumlah_pahami == buku:
    print('"Bu semua buka sudah dibaca dan di pahami')
else:
    print(f'"Bu , tidak semua buka bisa di pahami. '
          f'budi hanya memahami {jumlah_pahami} buku')
