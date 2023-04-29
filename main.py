"""
Semua sintaksis dasar bahasa pemograman terdiri dari :
1. sekuential : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali kali selama/sampai semua kondisi terpenuhi
"""

# SEKUENTIAL
print('Ibu Berkata", "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu Menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print("Maka budi berangkat ke toko")
print("dan mulai belanja")
print("================================")


"""
Soal: Ibu menyuruh anak membeli 1 botol susu, jika ada telur beli 6
      ibu bertanya kenapa membeli 6 botol susu
      anak menjaawab karena ada  telur
gimana cara nya membuat flow dan program anak membeli 1 botol susu dan 6 butir telur
"""

# Percabangan

jumlah_botol_susu = 173
jumlah_telur = 1487
print(f"Jumlah botol susu {jumlah_botol_susu} btl")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harga dan ternyata uang nya cukup")
    print("Budi membeli 1 botol susu")
    if jumlah_telur > 0:
        print("Budi membeli 6 butir telur")
    else:
        print("Budi Membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi Pulang kerumah")
print("Menyerahkan hasilnya kepada ibu")

