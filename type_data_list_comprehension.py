print('\nPrint List Comprehension')
print('\nPerintah Del')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprenhension')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
del daftar_buku[0:-1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start step')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
del daftar_buku[0:2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru')
daftar_buku = ['java', 'php', 'python','C++', 'golang']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
daftar_buku_baru.append('testing')
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan list comprehension ganjil dan genap ')
daftar_buku = ['1 java', '2 php', '3 python','4 C++', '5 golang']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan list comprehension : buang ujung ')
daftar_buku = ['1 java', '2 php', '3 python','4 C++', '5 golang']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan list comprehension ganjil  ')
daftar_buku = ['1 java', '2 php', '3 python','4 C++', '5 golang']
print(daftar_buku[0::2])