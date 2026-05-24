n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input(f'Masukkan nama kategori {i+1}: ')
    print(f'Masukkan 3 nama aplikasi di kategori {nama_kategori}')

    aplikasi = []
    for j in range(3):
        nama_aplikasi = input(f'Nama aplikasi {j+1}: ')
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print("\n", data_aplikasi)

aplikasi_satu_kategori = set()
aplikasi_dua_kategori = set()

for aplikasi in data_aplikasi.values():
    for app in aplikasi:
        if app in aplikasi_satu_kategori:
            aplikasi_dua_kategori.add(app)
        else:
            aplikasi_satu_kategori.add(app)

print("\nAplikasi yang hanya muncul di satu kategori saja:")
for app in aplikasi_satu_kategori:
    print(app)

if n > 2:
    print("\nAplikasi yang muncul tepat di dua kategori sekaligus:")
    for app in aplikasi_dua_kategori:
        print(app)

        