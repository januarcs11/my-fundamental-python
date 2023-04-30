daftar_buku = ['java', 'php', 'python']
print('Tampilkan variable data buku')
print(daftar_buku)


print('\nTampilkan semua data dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'januar', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data setiap element berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['java', 'php', 'python']
print('\nTambahkan 1 buku baru judul nya C++')
daftar_buku.append('C++')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Element Pertama')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
daftar_buku[0] = 'ReactJs'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil atau hilangkan element ke 2 disimpan ke variable')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[1])


print('\nTampilkan dari variable Buku yang diambil tadi element ke 2')
print(buku)

print('\nPop tanpa parameter, dari data list awal dan akhir data tidak ditampilkan')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPrint pop -1 untuk menghilangkan data dari akhir data di list maka data golang akan hilang')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])




